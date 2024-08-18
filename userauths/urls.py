from django.urls import path
from userauths import views

app_name = "userauths"

urlpatterns = [
    path("sign-up/",views.register_view,name="sign-up"),
    path('login/', views.login_view, name='login'),
    path('facebook-login/', views.facebook_login, name='facebook_login'), 
    path('google-login/', views.google_login, name='google_login'), 



]