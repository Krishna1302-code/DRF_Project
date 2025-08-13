from django.db import models # Base ORM tools
from django.contrib.auth.models import AbstractUser  # Base user model for authentication
import uuid  # For unique IDs
from phonenumber_field.modelfields import PhoneNumberField




class User(AbstractUser):
    full_name = models.CharField(max_length=100,default='abc')
    email = models.EmailField()
    phone = PhoneNumberField(unique = True ,blank = False,null=True)

    def __str__(self):
        return self.full_name

class Product(models.Model):

    GENDER_CHOICES=[
        ('F','FEMALE'),
        ('M','MALE'),
    ]

    name = models.CharField(max_length=100,null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    stock = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False,default='F')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)  

    @property
    def in_stock(self):
        return self.stock>0
   
    def __str__(self):
        return self.name

class Product_image(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
    image_url = models.ImageField(upload_to='product/')

class Address(models.Model):        
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='addresses')
    street = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Cart(models.Model):#this is intermediate table between cart and product for user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="Cart_Item")



class Cart_item(models.Model):#this is through table cuz of many to many relationship 
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey(Cart ,on_delete=models.CASCADE,related_name= 'cart_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_items")
    #ManyToManyRel is not meant to be used directly in models,
    #For a through table (Cart_Item), you should be using ForeignKey for both sides, not a ManyToManyField.

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name= 'review')
    rating = models.IntegerField()
    comments = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Order(models.Model):
     STATUS_CHOICE=[  
        ('PENDING','Pending'),
        ('CONFIRMED','Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ] 
     order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)#need to understand this like if django already providing it then why
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)
     price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
     subtotal = models.DecimalField(max_digits=10, decimal_places=2,default=0)
     total = models.DecimalField(max_digits=10, decimal_places=2,default=0)

     status = models.CharField(max_length=10,choices = STATUS_CHOICE, blank=False)
     products = models.ManyToManyField(Product,through="OrderItem",related_name='order')


     def __str__(self):
        return f"Order {self.order_id} by {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')

    quantity = models.PositiveIntegerField()

    @property
    def item_subtotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.order_id}"