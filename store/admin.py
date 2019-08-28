from django.contrib import admin
from store.models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(OrderProducts)