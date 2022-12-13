from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="home"),
    path('pricing/', views.pricing, name="pricing"),
    path('product/', views.product_cart, name="product"),
    path('contacts/', views.contacts, name="contacts"),
]
