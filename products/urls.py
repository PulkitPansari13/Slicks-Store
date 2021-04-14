from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('shop/<str:gender>/', views.shopgender, name='shop_gender'),
    path('shop/product/<str:uqid>/', views.product_detail, name='shop_product'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('cart/', views.cart, name='cart'),
    path('search/', views.search, name='search'),
    path('cart/step2/', views.addresspage, name='address_page'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('testurl/', views.testurl, name='testurl')
]

# url routes for ajax calls
urlpatterns += [
    path('api/wlist/toggle', views.wishlist_add_remove_product, name='wlist_toggle'),
    path('api/cart/add', views.addtocart, name='cart_add'),
    path('api/cart/remove', views.removefromcart, name='cart_remove'),
    path('api/cart/update', views.updatequant, name='cart_update')
]
