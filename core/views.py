from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from core.models import Product,ProductImages,ProductReview,CartOrder,Category,CartOrderItems,Vendor,Wishlist,Address


def index(request):
    # products = Product.objects.all().order_by("-id")
    products = Product.objects.filter(product_status="published",featured=True)
    
    context = {
        "products":products
        
    }
    return  render(request,"core/index.html",context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published",featured=True)
    
    context = {
        "products":products
        
    }
    return  render(request,"core/product-list.html",context)



def category_list_view(request):
    categories = Category.objects.all()
    
    context = {
        "categories":categories
    }
    
    return  render(request,"core/category-list.html",context)

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



