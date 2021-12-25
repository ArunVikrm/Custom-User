from django.urls import path
from .views import HomePage , SignUpPage , LoginPage , LogoutPage

urlpatterns = [
    path('',HomePage,name='HomePage'),
    path('signup/',SignUpPage,name='SignUp'),
    path('login/',LoginPage,name='Login'),
    path('logout/',LogoutPage,name='Logout'),
]
