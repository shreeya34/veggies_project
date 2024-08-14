from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return  render(request,"core/index.html")

def contact(request):
    return render(request, "core/contact.html")

def shop(request):
    return render(request,"core/shop.html")

def shop_details(request):
    return render(request,"core/shop-detail.html")