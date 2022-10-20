from django.shortcuts import render, redirect
from .forms import CreationForm, ChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    users = get_user_model().objects.all()
    context ={
        'users': users
    }
    return render(request, 'accounts/index.html', context)

def signup(request):
    if request.method =='POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/forms.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/forms.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def detail(request, pk):
    profile = get_user_model().objects.get(pk=pk)
    context = {
        'profile': profile
    }
    return render(request, 'accounts/detail.html', context)