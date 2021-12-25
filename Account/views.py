from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate, logout

from .forms import RegistrationForm , CustomerAuthenticationForm

def HomePage(request):
    context = {}
    return render(request , 'home.html' , context)

def SignUpPage(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request,email=email,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('HomePage')

    context ={
        'form' : form
    }

    return render(request,'signup.html' , context)

def LoginPage(request):
    form = CustomerAuthenticationForm()
    if request.method == 'POST':
        form = CustomerAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request,email=email,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('HomePage')
    context = {
        'form' : form
    }
    return render(request,'login.html',context)

def LogoutPage(request):
    logout(request)
    return redirect('HomePage')

