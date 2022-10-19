# TIL Project-Template

```python
class Articles(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFill(400, 200)],
                                    format='JPEG',
                                    options={'quality': 60})
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comments(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)

```

## INTRO

- 🗓 프로젝트 기간
  - 2022.10.19
- 💻 사용 기술
  - Python, Django, HTML, CSS, Bootstrap5
- ⭐ 나의 역할
  - 참조와 역참조를 이해하고 응용할 수 있다.
  - 
- 💡 배운 점
  - 1 : N 관계의 DB를 생성하고 외래키(Foriegn Key) 컬럼 모델을 작성할 수 있었다.
  - Comment 에서 User를 참조하고, User에서 Comment를 참조 할 수 있다. ( 참조, 역참조 )
  - 



## 🚩목적

> project's goal

- 참조와 역참조, 1 : N 관계 DB 생성
- 



# 🧾기능 소개

- Accounts 앱 에서 계정의 CRUD를 구현하고, 인증된 회원의 경우 Article과 Comment를 작성 할 수 있다.
- 회원은 여러개의 Article을 작성할 수 있으며, 하나의 Article은 여러개의 Comment를 가질 수 있다.
- 1: N  => 1: N

# 문제 해결

## 문제 상황

- request.user 로 현재 session에 저장된 user 의 정보를 꺼내 Article의 작성자와 대조하는 과정을 활용 할 수 있었다.
- view단으로 pk 값을 넘기는데 article의 pk와 comment의 pk와 user의 pk를 잘 구분짓는 것이 필요했다.



## 해결



```python

```