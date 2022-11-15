from django.shortcuts import render, redirect
from .forms import CreateUserForm, ChangeUserForm
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, pk):
    users = get_user_model().objects.get(pk=pk)
    context = {
        'users': users
    }
    return render(request, 'accounts/detail.html', context)

@login_required
def update(request, pk):
    users = get_user_model().objects.get(pk=pk)
    if request.method == 'POST':
        form = ChangeUserForm(request.POST, instance=users)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ChangeUserForm(instance=users)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

@login_required
def delete(request, pk):
    users = get_user_model().objects.get(pk=pk)
    users.delete()
    return redirect('articles:index')

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
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')
