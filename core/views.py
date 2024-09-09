from django.shortcuts import get_object_or_404, render
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



from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from core.models import Product, Category

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from core.models import Product, Category

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from core.models import Product, Category

def category_list_view(request):
    categories = Category.objects.all()
    print("Categories:", categories)  # Debugging line
    context = {"categories": categories}
    return render(request, "core/category-list.html", context)


def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    
    # Handle filtering by price range and tags
    price_filter = request.GET.get('price')
    tag_filter = request.GET.getlist('tag')

    products = Product.objects.filter(category=category)

    if price_filter:
        if price_filter == 'under50':
            products = products.filter(price__lt=50)
        elif price_filter == '50to100':
            products = products.filter(price__gte=50, price__lte=100)
        elif price_filter == 'above100':
            products = products.filter(price__gt=100)

    if tag_filter:
        if 'new' in tag_filter:
            # Example: Assume you have a field in Product for tags or similar
            products = products.filter(is_new=True) 
        if 'sale' in tag_filter:
            products = products.filter(on_sale=True) 
        if 'popular' in tag_filter:
            products = products.filter(is_popular=True)

    context = {
        'category': category,
        'products': products
    }
    return render(request, 'core/category-products.html', context)


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



