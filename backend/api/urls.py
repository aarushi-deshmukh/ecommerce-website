from django.urls import path
from .views import products, signin, signup_buyer, signup_seller
from . import views

urlpatterns = [
    path("products/", products),
    path("signin/", signin),
    path("signup/buyer/", signup_buyer),
    path("signup/seller/", signup_seller),
    path("products/", views.get_products),

    path("cart/", views.get_cart),
    path("cart/add/", views.add_to_cart),

    path("wishlist/", views.get_wishlist),
    path("wishlist/add/", views.add_to_wishlist),
]
