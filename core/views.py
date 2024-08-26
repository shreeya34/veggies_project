from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from core.models import Product,ProductImages,ProductReview,CartOrder,Category,CartOrderItems,Vendor,Wishlist,Address


def index(request):
    bananas = Product.objects.all()
    
    context = {
        "products":bananas
        
    }
    return  render(request,"core/index.html")

def contact(request):
    return render(request, "core/contact.html")

def shop(request):
    return render(request,"core/shop.html")

def shop_details(request):
    return render(request,"core/shop-detail.html")


def checkout(request):
    return render(request,"core/chackout.html")

def testimonial(request):
    return render (request,"core/testimonial.html")

def cart(request):

    return render(request, 'core/cart.html')



