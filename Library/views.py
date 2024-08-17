from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegistrationform
from .models import Book

# Create your views here.
def home(request):
    return render(request,'home.html')


def booklist(request):
    book = Book.objects.all()
    return render(request,'booklist.html',{'books':book})
def register(request):
    if request.method == 'POST':
        form = UserRegistrationform(request.POST)
        if form.is_valid():
            form.save()
            # Add success message
            messages.success(request, "You have registered successfully!")
            return redirect('home')
    else:
        form = UserRegistrationform()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('booklist')  # Redirect to the home page or another page
            else:
                # This case should not occur as form.is_valid() and authenticate() are used
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})