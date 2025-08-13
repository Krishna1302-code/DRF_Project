from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_product,name='list'),
    path('create/',views.create_product,name='create'),
    path('get/<int:pk>/',views.get_product,name='get'),
    path('update/<int:pk>/',views.update_product,name='update'),
    path('delete/<int:pk>/',views.delete_product,name='delete'),
]
