import csv
from store.models import Category,SubCategory,Product

data = csv.reader(open('/Users/Mahmoud Dawlatly/Documents/FYP/Product.csv', encoding='utf8'),delimiter=',')
a=0
for row in data:
    if row[0] != 'Product Category':
        product = Product()
        if row[0]=='Technology':
            product.product_Category_id = 3
        elif row[0] == 'Furniture':
            product.product_Category_id = 4
        elif row[0] == 'Office Supplies':
            product.product_Category_id = 2

        else:
            product.product_Category_id = 5
        if row[1]=='Telephones and Communication':
            product.product_SubCategory_id = 1
        elif row[1] == 'Office Machines':
            product.product_SubCategory_id = 2
        elif row[1] == 'Computer Peripherals':
            product.product_SubCategory_id = 3
        elif row[1] == 'Copiers and Fax':
            product.product_SubCategory_id = 4
        elif row[1] == 'Bookcases':
            product.product_SubCategory_id = 5
        elif row[1] == 'Chairs & Chairmats':
            product.product_SubCategory_id = 6
        elif row[1] == 'Tables':
            product.product_SubCategory_id = 7
        elif row[1] == 'Office Furnishings':
            product.product_SubCategory_id = 8
        elif row[1] == 'Paper':
            product.product_SubCategory_id = 9
        elif row[1] == 'Envelopes':
            product.product_SubCategory_id = 10
        elif row[1] == 'Appliances':
            product.product_SubCategory_id = 11
        elif row[1] == 'Labels':
            product.product_SubCategory_id = 12
        elif row[1] == 'Pens & Art Supplies':
            product.product_SubCategory_id = 13
        elif row[1] == 'Rubber Bands':
            product.product_SubCategory_id = 14
        elif row[1] == 'Scissors, Rulers and Trimmers':
            product.product_SubCategory_id = 15
        elif row[1] == 'Binders and Binder Accessories':
            product.product_SubCategory_id = 16
        else:
            product.product_SubCategory_id = 17
        product.product_Name = row[2]
        product.product_Price = row[3]
        product.save()

