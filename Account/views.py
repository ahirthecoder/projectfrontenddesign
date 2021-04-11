from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import RegistrationForm, LoginForm


def register_view(request):
    
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        
        else:
            context['registration_form'] = form
            
    else:  # GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)
    
    
def login_view(request):
    
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    
    context = {}
    if request.POST:
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')

    else:
        form = LoginForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)
    
    
def account_view(request):
    
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}  
    context['email'] = request.user.email
    context['api_key'] = request.user.api_key
    context['daily_limit'] = request.user.daily_limit

    return render(request, 'account/account.html', context)
    
    
def logout_view(request):
    
    logout(request)
    return redirect('home')

#1@XxYyZz
#1@AaBbCc