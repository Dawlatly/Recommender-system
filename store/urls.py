from django.conf.urls import url
from django.contrib.auth.views import password_reset,password_reset_done,password_reset_confirm,password_reset_complete
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^login',views.user_login, name='login'),
    url(r'^signup',views.register, name='register'),
    url(r'^logout',views.user_logout, name='logout'),
    url(r'^about',views.aboutus, name='aboutus'),
    url(r'^contact',views.contactus, name='contact'),
    url(r'^orders/(?P<username>\w+)',views.orders, name='orders'),
    url(r'^categoryList',views.categoryList, name='categories'),
    url(r'^delinfo/(?P<cartid>\d+)',views.deliveryInfo, name='checkout'),
    url(r'^confirm/(?P<cartid>\d+)',views.confirmOrder, name='confirm'),
    url(r'^subcategoryList/(?P<catid>\d)',views.subCategoryList, name='subcategoryList'),
    url(r'^subcategory/(?P<subcatid>\d+)',views.subCategory, name='productList'),
    url(r'^product/(?P<productid>\d+)',views.product,name='product'),
    url(r'^produc/(?P<productid>\d+)/(?P<username>\w+)',views.addToCart,name='addtocart'),
    url(r'^cart/(?P<username>\w+)',views.shoppingcart,name='shoppingcart'),
    url(r'^password-reset/$',password_reset),
    url(r'^password-reset/done/$',password_reset_done),
    url(r'^password-reset/confirm/$',password_reset_confirm,name='password_reset_confirm'),
    url(r'^password-reset/complete/$',password_reset_complete),
    url(r'^remove/(?P<productid>\d+)/(?P<username>\w+)',views.deleteFromCart,name='delete'),
]