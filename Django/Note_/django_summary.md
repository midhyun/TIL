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