from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Buyer, Seller, Product, Cart, CartItem, Wishlist
from .serializers import ProductSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import json
from rest_framework import status
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['GET'])
def products(request):
    items = Product.objects.all()
    serializer = ProductSerializer(items, many=True)
    return Response(serializer.data)

@csrf_exempt
def signin(request):

    if request.method != "POST":
        return JsonResponse({"success": False, "error": "Invalid request method"}, status=405)

    data = json.loads(request.body)

    email = data.get("email")
    password = data.get("password")
    account_type = data.get("account_type")

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse({"success": False, "error": "User not found"})

    # check password
    if not check_password(password, user.password):
        return JsonResponse({"success": False, "error": "Invalid password"})

    # check role
    if account_type == "Buyer":
        if not Buyer.objects.filter(user=user).exists():
            return JsonResponse({"success": False, "error": "Buyer account not found"})

    elif account_type == "Seller":
        if not Seller.objects.filter(user=user).exists():
            return JsonResponse({"success": False, "error": "Seller account not found"})
    else:
        return JsonResponse({"success": False, "error": "Invalid account type"})

    # GENERATE JWT TOKENS
    refresh = RefreshToken.for_user(user)

    return JsonResponse({
        "success": True,
        "user_id": user.id,
        "email": user.email,
        "account_type": account_type,
        "access": str(refresh.access_token),
        "refresh": str(refresh)
    })
    
@csrf_exempt
def signup_buyer(request):

    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=405)

    data = json.loads(request.body)

    if User.objects.filter(email=data["email"]).exists():
        return JsonResponse({"error": "User already exists"})

    user = User.objects.create_user(
        username=data["username"],
        email=data["email"],
        password=data["password"],
        first_name=data["first_name"],
        last_name=data["last_name"]
    )

    Buyer.objects.create(
        user=user,
        age=data["age"],
        phone_number=data["phone_number"],
        address=data["address"],
        city=data["city"],
        country=data["country"],
        pincode=data["pincode"]
    )

    return JsonResponse({"message": "Buyer account created successfully"})

@csrf_exempt    
def signup_seller(request):

    if request.method == "POST":

        data = json.loads(request.body)

        user = User.objects.create_user(
            username=data["email"],
            email=data["email"],
            password=data["password"]
        )

        Seller.objects.create(
            user=user,
            company_name=data["company_name"],
            contact_number=data["contact_number"],
            address=data["address"],
            city=data["city"],
            country=data["country"],
            pincode=data["pincode"]
        )

        return JsonResponse({
            "message": "Seller account created successfully"
        })
    
@csrf_exempt
def get_products(request):

    products = Product.objects.all()

    data = []

    for p in products:
        data.append({
            "id": p.id,
            "name": p.name,
            "price": float(p.price),
            "quantity": p.stock,
            "category": p.category,
            "image": p.image.url if p.image else ""
        })

    return JsonResponse(data, safe=False)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    print("AUTH HEADER:", request.headers.get("Authorization"))
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Login required"}, status=401)

    if request.method == "POST":

        data = json.loads(request.body)

        product_id = data.get("product_id")
        quantity = data.get("quantity", 1)

        buyer = Buyer.objects.get(user=request.user)

        product = Product.objects.get(id=product_id)

        # get or create cart
        cart, created = Cart.objects.get_or_create(buyer=buyer)

        # get or create cart item
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()

        return JsonResponse({"message": "Added to cart"})    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_cart(request):

    if not request.user.is_authenticated:
        return JsonResponse({"error": "Login required"}, status=401)

    buyer = Buyer.objects.get(user=request.user)

    cart = Cart.objects.filter(buyer=buyer).first()

    if not cart:
        return JsonResponse({"items": []})

    items = CartItem.objects.filter(cart=cart)

    data = []

    for item in items:
        data.append({
            "product_id": item.product.id,
            "name": item.product.name,
            "price": float(item.product.price),
            "quantity": item.quantity,
            "image": item.product.image.url if item.product.image else None
        })

    return JsonResponse({"items": data})

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_wishlist(request):

    data = request.data
    product_id = data.get("product_id")

    buyer = Buyer.objects.get(user=request.user)

    product = Product.objects.get(id=product_id)

    Wishlist.objects.get_or_create(
        buyer=buyer,
        product=product
    )

    return Response({"message": "Added to wishlist"})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_wishlist(request):

    if not request.user.is_authenticated:
        return JsonResponse({"error": "Login required"}, status=401)

    buyer = Buyer.objects.get(user=request.user)

    items = Wishlist.objects.filter(buyer=buyer)

    data = []

    for item in items:
        data.append({
            "product_id": item.product.id,
            "name": item.product.name,
            "price": float(item.product.price),
            "image": item.product.image.url if item.product.image else None
        })

    return JsonResponse({"items": data})

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, product_id):

    try:
        buyer = Buyer.objects.get(user=request.user)

        cart = Cart.objects.get(buyer=buyer)

        cart_item = CartItem.objects.get(
            cart=cart,
            product_id=product_id
        )

        cart_item.delete()

        return Response({"message": "Item removed from cart"})

    except CartItem.DoesNotExist:
        return Response(
            {"error": "Item not found in cart"},
            status=status.HTTP_404_NOT_FOUND
        )
    
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def remove_from_wishlist(request, product_id):

    try:
        buyer = Buyer.objects.get(user=request.user)

        wishlist_item = Wishlist.objects.get(
            buyer=buyer,
            product_id=product_id
        )

        wishlist_item.delete()

        return Response({"message": "Item removed from wishlist"})

    except Wishlist.DoesNotExist:
        return Response(
            {"error": "Item not found in wishlist"},
            status=status.HTTP_404_NOT_FOUND
        )
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request):

    buyer = Buyer.objects.get(user=request.user)

    return Response({
        "name": request.user.first_name + " " + request.user.last_name,
        "email": request.user.email,
        "phone": buyer.phone_number,
        "address": buyer.address,
        "city": buyer.city,
        "country": buyer.country,
        "pincode": buyer.pincode
    })