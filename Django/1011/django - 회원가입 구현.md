### django - 회원가입 구현

```python
# urls.py
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup')
]
# views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    # POST 요청 처리
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
	    form = UserCreationForm()
    context ={
        'form': form
    }
    return rend(request, 'accounts/signup.html', context)
```

```html
{% extends 'base.html' %}
{% load bootstrap5 %}
{% block body %}
<h1>
    회원가입
</h1>
{{ bootstrap.form from }}
{% endblock body %}
```

