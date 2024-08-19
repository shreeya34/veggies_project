from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login as auth_login, authenticate,logout
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings

from userauths.models import User

def facebook_login(request):
    # Your Facebook login logic here
    return HttpResponse("Facebook login functionality here.")

def google_login(request):
    # Your Google login logic here
    return HttpResponse("Google login functionality here.")

def register_view(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Hey{username},your account was register")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password = form.cleaned_data['password1'])
            
            login(request,new_user)
            return redirect("core:index")
            
    else:
        print("User cannot be registered")
        form = UserRegisterForm()
    
    context = {
        'form':form
        
    }
    return render(request,"userauths/sign-up.html",context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "Hey, you are already logged in")
        return redirect("core:index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.warning(request, f"User with {email} does not exist")
            return render(request, "userauths/sign-in.html")

        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "You are logged in")
            return redirect("core:index")
        else:
            messages.warning(request, "Invalid credentials, please try again")
            
    return render(request, "userauths/sign-in.html")
            
def logout_view(request):
        logout(request)
        messages.success(request,"You logged out")
        return redirect("userauths:sign-in")
   