from django.contrib import admin
from  .models import Product,Category,Order,OrderItem 

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description','price','stock','image']

admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category,CategoryAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id','user', 'created_at', 'status']

admin.site.register(Order,OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(OrderItem,OrderItemAdmin)