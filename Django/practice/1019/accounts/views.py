from django.shortcuts import render, redirect
from .forms import UserForm, UserFormUpdate
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/forms.html', context)

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user':user
    }
    return render(request, 'accounts/detail.html', context)


@login_required
def update(request, pk):
    if request.user.pk == pk:
        user = get_user_model().objects.get(pk=pk)
        if request.method == 'POST':
            form = UserFormUpdate(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            form = UserFormUpdate(instance=user)
        context = {
            'form': form
        }
        return render(request, 'accounts/forms.html', context)
    else:
        return redirect('accounts:error')

@login_required
def delete(request, pk):
    if request.user.pk == pk:
        user = get_user_model().objects.get(pk=pk)
        user.delete()
        auth_logout(request)
        return redirect('articles:index.html')
    else:
        return redirect('accounts:error')

def error(request):
    return render(request, 'accounts/error.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/forms.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')