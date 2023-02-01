장고 서버를 구동하기 위해 지금까지는 `python manage.py runserver` 처럼 장고의 내장 서버를 구동하는 방식을 사용했다.
```
장고의 내장서버

웹 서버와 WSGI 서버의 기능을 모두 포함하고 있다. 다만 내장 서버는 기능이 단순하고 '대량 요청'이나 '동시 요청'을 효율적으로 처리하지 못하므로 운영 환경에는 적합하지 않다.
```

개발 환경이 아닌 운영 환경에서 어떻게 웹 서버와 WSGI 서버를 구성해야 하는지 알아야 한다.

### 웹 브라우저
<hr>
사용자는 시스템에 접속하기 위해 웹 브라우저를 이용하여 홈페이지에 접속한다. 이 때 웹 브라우저는 웹 서버에 페이지를 요청한다.

웹 브라우저가 웹 서버에 요청하는 페이지는 크게 두 가지로 분류된다.
1. 정적 페이지
2. 동적 페이지

#### 정적(static) 페이지
웹 브라우저로 URL을 요청한다면, 서버의 정적 파일을 읽어서 리턴한다.
파일은 변하지 않는 동일한 값을 리턴할 것이다. 확장자 명이 js인 자바스크립트나 jpg, png와 같은 이미지 파일도 마찬가지이다. 이런 파일들을 정적 파일(static file)이라고 한다.

이렇게 웹 브라우저에서 css, js, jpg, png와 같은 정적 파일을 요청하는 것을 정적페이지 요청이라고 한다.

#### 동적(dynamic) 페이지
이번에는 웹 브라우저가 게시판 페이지를 요청하는 경우를 생각해 보자. 서버는 이런 요청이 들어오면 게시판 목록을 조회하여 리턴한다. 이때 응답 데이터인 게시판 목록은 데이터베이스의 내용에 따라 수시로 변한다.

이렇게 응답이 수시로 변하는 요청을 **동적 페이지 요청** 이라고 한다.

### 웹 서버(Web Server)
<hr>
웹 서버는 웹 브라우저의 정적 요청과 동적 요청을 처리하는 서버이다.
> 대표적인 웹 서버에는 아파치(`Apache`), 엔진엑스(`Nginx`) 등이 있다. 장고는 가장 잘 어울리는 엔진엑스(`Nginx`)를 웹 서버로 사용한다.

웹 서버에 정적 페이지 요청이 들어오면 정적 파일을 읽어 응답하면 되므로 간단하다.

하지만 동적 페이지 요청은 조금 복잡하다.

웹 서버에 동적 페이지 요청이 들어오면 웹 서버는 파이썬 프로그램을 호출해야 한다. 예를 들어 질문 목록 페이지 요청이 들어오면 질문 목록을 조회하여 리턴하는 파이썬 프로그램을 호출해야 한다. 하지만 대부분의 웹 서버는 파이썬 프로그램을 호출할 수 있는 기능이 없다. 어떻게 파이썬 프로그램을 호출해야 하는지 모르기 때문이다.

이러한 이유로 파이썬 프로그램을 호출하는 WSGI(Web Server Gateway Interface)서버가 반드시 필요하다. 웹 서버에 동적 요청이 발생하면 웹 서버가 WSGI 서버를 호출하고, WSGI 서버는 파이썬 프로그램을 호출하여 동적 페이지 요청을 대신 처리하는 것이다.

### WSGI 서버
<hr>
WSGI 서버는 웹 서버가 동적 페이지 요청을 처리하기 위해 호출하는 서버이다. WSGI 서버에는 여러 종류가 있지만 `Gunicorn` 과 `uwsgi`를 가장 많이 사용한다.

웹 서버에 동적 페이지 요청이 발생하면 웹 서버는 WSGI 서버를 호출하고 WSGI 서버는 다시 WSGI 애플리케이션을 호출한다. 여기서 알 수 있는 중요한 사실은 실제 동적 페이지 요청은 결국 WSGI 애플리케이션이 처리한다는 점이다. WSGI 애플리케이션이 처리한다는 점이다. WSGI 애플리케이션에는 장고(Django), 플라스크(Flask) 등이 있다. 파이보 시스템이 사용할 WSGI 애플리케이션은 현재 사용하는 장고이다.

> WSGI 서버는 웹 서버와 WSGI 애플리케이션 중간에 위치한다. 그래서 WSGI서버는 WSGI 미들웨어(middleware) 또는 WSGI 컨테이너(container) 라고도 한다.

### WSGI 애플리케이션
<hr>
WSGI 서버는 항상 다음파일을 경유하여 장고(django) 프로그램을 호출한다.
`[파일명: projects\mysite\config\wsgi.py]`
```
import os
from django.core.wsgi import get_wsgi_application

os.environ.serdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()
```
이 파일에 선언된 `application`이 바로 장고의 애플리케이션이다. 이 파일은 장고 프로젝트 생성시 자동으로 만들어지며 특별한 경우가 아니고는 수정할 필요가 없다.

### WSGI 순서도
<hr>
지금까지의 내용을 그림으로 나타내면 다음과 같다.
![[Pasted image 20230131171059.png]]
웹 브라우저의 정적 페이지 요청은 웹 서버가 처리하고, 동적 페이지 요청은 [WSGI 서버 -> WSGI 애플리케이션]으로 처리한다.

### Gunicorn
<hr>
웹 서버에서 파이선 장고 애플리케이션을 호출하려면 WSGI 서버가 필요하다고 했다. 
> Gunicorn은 구니콘이라고 읽는다.

WSGI 서버의 양대산맥으로 Gunicorn과 uwsgi가 있다. 과거에는 "성능은 uwsgi가 앞서고 편의성은 Gunicorn이 좋다."라는 의견들이 많았는데 최근에는 Gunicorn의 성능이 매우 좋아졌기 때문에 Gunicorn을 사용하는 사람들이 점점 더 많아지는 추세이다.

Gunicorn은 개발이 아니라 서버에 필요한 도구이므로 로컬 환경에서는 설치할 필요가 없다. 서버환경에 Gunicorn을 설치하면 된다. 터미널 클라이언트로 AWS서버에 가상환경을 이용하여 설치한다.

### Nginx
<hr>
웹 서버(Web Server)는 브라우저의 정적 페이지 요청을 처리하고 동적 페이지 요청인 경우 WSGI 서버를 호출하는 역할을 한다.

```
Nginx

높은 성능을 위해서 개발된 웹 서버로 점점 사용자가 증가하는 추세이다. 특히 파이썬 웹 프레임워크인 장고나 플라스크등에서 주로 사용된다. 또한 Nginx는 설정도 무척 간단하여 쉽게 사용할 수 있다.
```

참고: https://blog.neonkid.xyz/249
		https://tibetsandfox.tistory.com/22