from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserRegisterForm , UserLoginForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        my_form = UserRegisterForm(request.POST)
        if my_form.is_valid():
            my_form.save()
            return redirect('blog-home')
    else:
            my_form = UserRegisterForm()
            
    return render(request, 'users/register.html', {'form':my_form})

def login(request):
    if request.method == 'POST':
        my_form2 = UserLoginForm(request.POST)
        if my_form2.is_valid():
            my_form2.save()
            return redirect('blog-home')
    else:
            my_form2 = UserLoginForm()
            
    return render(request, 'users/login.html', {'form':my_form2})
