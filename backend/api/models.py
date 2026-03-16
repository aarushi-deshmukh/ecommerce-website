from django.db import models
from django.contrib.auth.models import User

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)

    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    company_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)

    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.company_name
    

class Product(models.Model):

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=255)
    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    stock = models.IntegerField()

    category = models.CharField(max_length=100, null=True, blank=True)

    image = models.ImageField(upload_to="products/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):

    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.buyer.user.username} Cart"
    
class CartItem(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    quantity = models.IntegerField(default=1)

    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    
class Wishlist(models.Model):

    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.buyer.user.username} - {self.product.name}"