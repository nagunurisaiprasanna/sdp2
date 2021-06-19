from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')

def signup(request):
     return render(request,'users\signup.html')

def home(request):
     return render(request,'users\home.html')

def contactus(request):
     return render(request,'users\contactus.html')

def Aboutus(request):
     return render(request,'users\Aboutus.html')

def signup2(request):
     return render(request,'users\signup2.html')
