from django.contrib import admin

from .models import *

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user')


admin.site.register(Customer, CustomerAdmin)

# admin.site.register(Man)
# admin.site.register(Women)
# admin.site.register(Kid)
admin.site.register(Brand)
admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'price', 'category', 'size', 'status', 'is_featured', 'is_new', 'accessories', 'is_man', 'is_women', 'is_kid')
    list_editable = ('status', 'price', 'category', 'size', 'brand', 'name', 'is_featured', 'is_new', 'accessories', 'is_man', 'is_women', 'is_kid' )
admin.site.register(Product, ProductAdmin)


admin.site.register(Accessories)
admin.site.register(Size)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity')

# admin.site.register(OrderItem, OrderAdmin)

class ShippingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'address', 'city', 'state', 'zipcode')

admin.site.register(ShippingAddress, ShippingAdmin)
# admin.site.register(Order)
admin.site.register(Ordered, OrderAdmin)