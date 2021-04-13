from django.contrib import admin

from .models import Product, Cart, CartItems, Orders, OrderItems
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'category',
                    'gender', 'sm_quant', 'm_quant', 'l_quant', 'xl_quant')


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'total_quant',  'payment_status',
                    'status', 'ordered_at', 'razorpay_order_id')


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'size',  'quant',
                    'item_price')



admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderItems, OrderItemsAdmin)
