from django.contrib import admin
from  .models import Product, Category, Order, OrderItem, Product_image, Address, Cart, Cart_item, Review

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description','price','stock','gender','category']

@admin.register(Product_image)
class Product_imageAdmin(admin.ModelAdmin):
    list_display = ['product']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display =['user','street','city','state','country','pincode']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductInline(admin.TabularInline):
    model = Cart.products.through  # Access the M2M table

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [ProductInline]



@admin.register(Cart_item)
class Cart_itemAdmin(admin.ModelAdmin):
   list_display = ['cart', 'product', 'quantity']
   list_filter = ['cart', 'product']
   search_fields = ['product__name', 'cart__user__username']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'rating', 'comments','created_at']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at', 'show_items')

    def show_items(self, obj):
        return ", ".join([item.name for item in obj.items.all()])
    show_items.short_description = "Items"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','product','quantity']
