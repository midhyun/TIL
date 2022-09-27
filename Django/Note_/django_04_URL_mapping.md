# App URL Mapping

> 앱이 많아졌을 때 urls.py 를 각 app 에 매핑하는 방법을 이해하기

### AppURLmapping

- 여러개의 app, 그 앱들의 view 함수가 많아지면서 사용하는 path() 또한 많아지기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음
- 각 앱의 view 함수를 다른 이름으로 import 할 수 있음

```python
from articles import views as articles_views
from pages import views as pages_views
# 좋은 방법은 아님
```

- 하나의 프로젝트에 여러 앱이 존재한다면, 각각의 앱 안에 urls.py를 만들고 프로젝트 urls.py에서 각 앱의 urls.py파일로 URL 매핑을 '위탁'할 수 있음.

- 각각의 app 폴더 안에 urls.py를 작성한다.
  ```python
  # project/urls.py
  from djangourls import path, include
  
  urlpatterns = [
      path('app1/', include('app1.urls'))
  ]
  
  # app1/urls.py
  from djanog.urls import path
  
  urlpatterns = [
      path('index/', views.index)
  ]
  ```

- urlpattern은 언제든지 다른 URLconf 모듈을 포함(include) 할 수 있음

  - include되는 앱의 urls.py에 urlpatterns가 작성되어 있지 않다면 에러가 발생함, 빈리스트라도 있어야 함.

### include()

- 다른 URLconf(app1/urls/py)들을 참조 할 수 있도록 돕는 함수.
- 함수 include()를 만나게 되면 URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달
- 즉 각각의 앱에서 URL을 관리한다.