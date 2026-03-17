from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    # AUTH
    path("signin/", views.signin),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("signup/buyer/", views.signup_buyer),
    path("signup/seller/", views.signup_seller),
    path("profile/", views.profile),

    # PRODUCTS
    path("products/", views.get_products),

    # CART
    path("cart/", views.get_cart),
    path("cart/add/", views.add_to_cart),
    path("cart/remove/<int:product_id>/", views.remove_from_cart),

    # WISHLIST
    path("wishlist/", views.get_wishlist),
    path("wishlist/add/", views.add_to_wishlist),
    path("wishlist/remove/<int:product_id>/", views.remove_from_wishlist),

]