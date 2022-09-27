# Template namespace

### 개요

- Django는 기본적으로 app_name/templates/ 경로에 잇는 templates 파일들만 찾을 수 있으며, settings.py의 INSTALLED_APPS에 작성한 app 순서로 template을 검색 후 렌더링 함.
- 바로 이 속성 값이 해당 경로를 활성화 하고 있음

### 디렉토리 생성을 통해 물리적인 이름공간 구분

- django templates의 기본 경로에 app과 같은 이름의 폴더를 생성해 폴더 구조를 app_name/templates/app_name/ 형태로 변경

- django templates의 기본 경로 자체를 변경할 수는 없기 때문에 물리적으로 이름 공간을 만드는 것
  ```python
  app1 / templates / app1 / index.html ...
  app2 / templates / app2 / index.html ...
  ```

### 템플릿 경로 변경

- 폴더 구조 변경 후 변견도니 경로로 해당항는 모든 부분을 수정해야함.
  ```python
  # app1 / views.py
  def index(request):
      return render(request, 'app1/index.html')
  # app2 / views.py
  def index(request):
      return render(request, 'app2/index.html')
  ```

  

- 반드시 Template namespace를 고려해야 할까?
  - 만약 단일앱으로만 이루어진 프로젝트라면 상관이 없음.
  - 여러 앱이 되었을 때에도 템플릿 파일 이름이 겹치지 않게 하면 되지만, 앱이 많아지면 대부분은 같은 이름의 템플릿 파일이 존재하기 마련

