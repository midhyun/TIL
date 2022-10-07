# django

> 웹 프레임 워크 ( 서버 ) - 파이썬 기반

- HTTP 서버 - 클라이언트 모델
  - URL 요청을 받아서
  - 처리하고 ( views.py ) - > 모델 활용
  - 응답을 해준다. ( Template )

## 개발 환경 ( 가상환경 ) 세팅!

>  가상환경 및 django 설치!

1. 가상환경 생성 및 실행

   ```bash
   $ python -m venv venv
   $ source venv/Scripts/activate
   ```

2. django 설치 및 기록

   ```bash
   $ pip install django==3.2.13
   $ pip freeze > requirements.txt
   ```

3. django 프로젝트 생성

   ```bash
   $ django-admin startproject pjt .
   ```

4. django app 생성

   ```bash
   $ python manage.py startapp articles
   ```

   - settings.py 앱 등록

   - urls.py 설정 ( urlpatterns ) 

     ```python
     # pjt/urls.py
     urlpatterns = [
         ...
         path('articles/', include('articles.urls')),
     ]
     # articles/urls.py
     from django.urls import path 
     from . import views
     
     app_name = 'articles'
     
     urlpatterns = [
       # http://127.0.0.1:8000/articles/
       path('', views.index, name='index'),
       ...
     ]
     ```

     

### Model 정의 (DB 설계)

##### 1.  클래스 정의

```python
class Article(models.Model):
    title = models.CharFieldl(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

#### 2. 마이그레이션 파일 생성

- app 폴더 내의 `migrations` 폴더에 생성된 파일 확인

```bash
$ python manage.py makemigrations
```

#### 3. DB 반영 (`migrate`)

```bash
$ python manage.py migrate
```

#### 4. CRUD 기능 구현

##### 0. ModelForm 선언

> 선언된 모델에 따른 필드 구성 (1) Form 생성(2) 유효성 검사

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'content']
```

##### 1. 게시글 생성

> 사용자에게 HTML Form 제공, 입력받은 데이터를 처리 (ModelForm 로직으로 변경)

##### 1. HTML Form 제공

> GET http://127.0.0.1:8000/articles/create/

(1) urls.py

(2) views.py

```python
def create(request):
    article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'artricles/create.html', context)
```

(3) articles/create.html

- HTML Form 태그 활용시 핵심
  - 어떤 필드를 구성할 것인지(`name`, `value`)
  - 어디로 보낼 것인지 (`action`, `method`)

```html
<h1>글쓰기</h1>
<form action="" method="POST">
  {% csrf_token %}
  {{ article_form.as_p }}
  <input type="submit" value="글쓰기">
</form>
```

##### 2. 입력받은 데이터 처리

> POST http://127.0.0.1:8000/article/create/
>
> 게시글 DB에 생성하고 index 페이지로 redirect

(1) urls.py

(2)views.py

- GET 요청 처리 흐름
- POST 요청 처리 흐름(주의! invalid)

```python
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(Request, 'articles/new.html', context)
```

### 2. 게시글 목록

> DB에서 게시글을 가져와서, template에 전달

### 3. 상세보기

> 특정한 글을 본다.

> http://127.0.0.1:8000/articles/int:pk/

### 4. 삭제하기

> 특정한 글을 삭제한다.

> http://127.0.0.1:8000/articles/int:pk/delete/

### 5. 수정하기

> 특정한 글을 수정한다. => 사용자에게 수정할 수 양식을 제공하고(GET) 특정한 글을 수정한다.(POST)

> http://127.0.0.1:8000/articles/int:pk/update/

## 추천 문서

- [HTTP request & response object](https://docs.djangoproject.com/en/4.1/ref/request-response/)
- [ModelForm](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/)
- [Django view shortcut functions](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/)
