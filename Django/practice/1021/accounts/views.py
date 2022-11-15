from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from articles.models import Review
from .forms import (
    UserCustomCreationForm,
    UserCustomChangeForm,
    UserCustomPasswordChangeForm,
)


# 회원가입
def signup(request):
    if request.method == "POST":
        form = UserCustomCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = UserCustomCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


# 로그인
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "articles:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


# 로그아웃
@login_required
def logout(request):
    auth_logout(request)
    return redirect("articles:index")


# 회원수정
@login_required
def accounts_update(request, pk):
    user = get_user_model().objects.get(pk=pk)
    if user == request.user:
        if request.method == "POST":
            form = UserCustomChangeForm(
                request.POST, request.FILES, instance=request.user
            )
            if form.is_valid():
                form.save()
                return redirect("accounts:detail", request.user.pk)
        else:
            form = UserCustomChangeForm(instance=request.user)
        context = {
            "form": form,
        }
        return render(request, "accounts/accounts_update.html", context)
    else:
        return redirect("articles:error")


# 비번수정
@login_required
def password_update(request):
    if request.method == "POST":
        form = UserCustomPasswordChangeForm(request.POST, request.user)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accounts:detail", request.user.pk)
    else:
        form = UserCustomPasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/password_update.html", context)


# 프로필
@login_required
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    review = user.review_set.all()
    context = {
        "user": user,
        "review": review,
    }
    return render(request, "accounts/detail.html", context)
