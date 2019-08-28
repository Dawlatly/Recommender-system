from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from store.forms import UserForm,CustomerForm
from store.models import *
import apriori
import random

PRDS = []
# Create your views here.
def index(request):
    return render(request, 'home.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        customer_form = CustomerForm(data=request.POST)

        if user_form.is_valid() and customer_form.is_valid() and user_form.cleaned_data['password'] == customer_form.cleaned_data['confirm_password'] and customer_form.cleaned_data['age'] > 0:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            customer = customer_form.save(commit=False)
            customer.confirm_password = ''
            customer.user = user
            customer.save()

            cart = Cart()
            cart.cart_Customer_id = customer.id
            cart.save()

            registered = True
        else:
            if customer_form.cleaned_data['age'] == 0:
                customer_form.add_error('confirm_password', "Age is incorrect.")
            else:
                customer_form.add_error('confirm_password',"Passwords do not match")
    else:
        user_form = UserForm()
        customer_form = CustomerForm()

    return render(request,'signup.html',{'user_form':user_form,'customer_form':customer_form,'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:

            return HttpResponse("Invalid login details")
    else:
        return render(request, 'login.html',{})


def categoryList(request):
    cat = Category.objects.all()
    return render(request,'categoryList.html',{'categoryList': cat})


def subCategoryList(request,catid):
    subcat = SubCategory.objects.all()
    subcat = subcat.filter(category=catid)
    return render(request,'subCategoryList.html',{'subcategoryList': subcat})

def subCategory(request,subcatid):
    prodct = Product.objects.all()
    prodct = prodct.filter(product_SubCategory=subcatid)
    return render(request,'subcategory.html',{'productList': prodct})

def product(request,productid):
    recItems = []
    rhs = apriori.finalRhs
    lhs = apriori.finalLhs
    allProducts = Product.objects.all()
    p = Product.objects.all()
    s = SubCategory.objects.all()
    p = list(p.filter(product_Id=productid))
    for i in range(0,lhs.__len__()):
        if p[0].product_SubCategory.subcategory_Name == lhs[i]:
            for j in range(0,rhs[i].__len__()):
                recItems.append(random.sample(list(allProducts.filter(product_SubCategory__subcategory_Name=rhs[i][j])),2))
    recItems = [item for sublist in recItems for item in sublist]
    return render(request,'productPage.html',{'product':p, 'recItems':recItems})

def addToCart(request,productid,username):
    p = Product.objects.all()
    p = list(p.filter(product_Id=productid))

    c = Cart.objects.all()
    c = list(c.filter(cart_Customer__user__username=username))
    c[0].cart_Products.add(p[0])
    return HttpResponse(status=204)

def deleteFromCart(request,productid,username):
    p = Product.objects.all()
    p = list(p.filter(product_Id=productid))

    c = Cart.objects.all()
    c = list(c.filter(cart_Customer__user__username=username))
    c[0].cart_Products.remove(p[0])
    return HttpResponseRedirect(reverse('shoppingcart',kwargs={'username':username}))


def shoppingcart(request,username):
    c = Cart.objects.all()
    c = list(c.filter(cart_Customer__user__username=username))
    c=c[0]
    return render(request,'cart.html',{'cart':c})

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')

def orders(request,username):
    l = []
    oo = Order.objects.all()
    oo = list(oo.filter(order_Customer__user__username=username))
    o = OrderProducts.objects.all()
    o = o.filter(order__order_Customer__user__username=username)
    for i in oo:
        l.append(list(o.filter(order_id=i.order_Id)))
        print(l[0][0].product.product_Name)

    return render(request, 'orderPage.html',{'products':l,'orders':oo})

def deliveryInfo(request,cartid):
    c = Cart.objects.all()
    c = list(c.filter(id=cartid))
    c = c[0]
    c = c.cart_Products.all()

    data = request.POST
    convertedData = dict(data)
    quantity = convertedData['quantity']

    toKeep = []
    finalCart= []
    ids=[]
    total = 0

    for i in range(0,len(quantity)):
        if int(quantity[i]) != 0:
            toKeep.append(quantity[i])
            finalCart.append(c[i])
            ids.append(c[i].product_Id)
            total += (c[i].product_Price * int(quantity[i]))

    if  len(finalCart):
        request.session['aaa']=ids
        global PRDS
        PRDS = finalCart

    else:
        return HttpResponse(status=204)
    toKeep.reverse()
    return render(request, 'checkout.html', {'products': finalCart, 'quantity':toKeep,'total':total,'cartId':cartid})

def confirmOrder(request,cartid):
    ids=request.session.get('aaa')
    print(ids)
    c = Cart.objects.all()
    order = Order()
    c = list(c.filter(id=cartid))
    c = c[0]

    order.order_Customer = c.cart_Customer



    data=request.POST
    total = request.POST.get('total')
    address1 = request.POST.get('address1')
    address2 = request.POST.get('address2')
    city = request.POST.get('city')
    state = request.POST.get('state')
    zipcode = request.POST.get('zipcode')

    convertedData = dict(data)
    tempQuantity = convertedData['quantity']
    print(total)



    order.order_Total = total
    c.cart_Customer.address = address1
    c.cart_Customer.address2 = address2
    c.cart_Customer.city = city
    c.cart_Customer.state = state
    c.cart_Customer.zipcode = zipcode
    c.cart_Customer.save()
    c.cart_Products.clear()
    print(tempQuantity)
    quantity = []
    for i in range(0,len(tempQuantity)):
        quantity.append(tempQuantity[i])

    global PRDS
    products = PRDS

    print(quantity[0])
    order.save()

    p = Product.objects.all()
    products = []

    for z in range(0,ids.__len__()):
        products.append(p.filter(product_Id=ids[z]))

    for j in range(0,products.__len__()):
        orderproducts = OrderProducts()
        orderproducts.product = products[j][0]
        orderproducts.quantity = quantity[0][j]
        orderproducts.order = order
        orderproducts.save()

    PRDS = []
    print(PRDS)
    return HttpResponse(status=204)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))