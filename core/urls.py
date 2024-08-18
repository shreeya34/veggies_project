from django.urls import path

from core import views
from core.views import index

app_name = "urls"
urlpatterns = [
    path("", views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('shop/',views.shop, name="shop"),
    path('shop_details/',views.shop_details, name="shop_details"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout, name="checkout"),
    path('testimonial/',views.testimonial,name="testimonial"),
  
   


    
    
]