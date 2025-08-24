# accounts/views.py 

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.shortcuts import render

@login_required
def dashboard(request):

    return render(request, 'accounts/dashboard.html')



def register_view(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been successfully created! Welcome.')
            return redirect('home')
        else:
            messages.error(request, ('pls you solve error ,and try again.'))
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'welcome، {username}!')
                return redirect('home')
            else:
                messages.error(request, 'username or password is fail.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    
    logout(request)
    messages.info(request, 'You have successfully logged out of the site.')
    return redirect('accounts:login')

# It's for a test

class MyBookingForm(forms.Form):
    name = forms.CharField(label='full name', max_length=100)
    email = forms.EmailField(label='email')
    booking_date = forms.DateField(label='Reservation date', widget=forms.DateInput(attrs={'type': 'date'}))
    



def book_now_view(request):
   
    if request.method == 'POST':
        form = MyBookingForm(request.POST)
        if form.is_valid():
            #Here you can save form data or perform other operations
            messages.success(request, 'Your reservation has been successfully made!')
            return redirect('home') #Or to a booking confirmation page
        else:
            messages.error(request, 'Please fix the errors in the booking form.')
    else:
        form = MyBookingForm()
    return render(request, 'book_now.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class CustomRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = '/accounts/login/'
    
def login_register_view(request):
    login_form = AuthenticationForm()
    register_form = UserCreationForm()
    
    context = {
        'login_form': login_form,
        'register_form': register_form
    }
    return render(request, 'accounts/login_register.html', context)