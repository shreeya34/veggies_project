from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

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
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to a success page
    else:
        form = AuthenticationForm()
    return render(request, 'userauths/login.html', {'form': form})