### 좋아요 기능

> ManyToManyField, symmetrical 속성

```python
# models.py
from djagno.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # followings, user모델 자신과, 단방향,(symmetricla = True 양방향노드),
```



```python
# views.py - 좋아요 기능과 유사함
@login_required
def follow(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk) # get 오류 발생시 404에러 출력
    if request.user == user:
        messages.warning(request, '스스로 팔로우 할 수 없습니다.') # 1->1 경우 방지
        return redirect('accounts:detail', pk)
    if request.user in user.followers.all(): # 이미 팔로우 중이라면
        user.followers.remove(request.user)  # 팔로우 제거
    else:
        user.followers.add(request.user)	 # 아니라면 팔로우
	return redirect('accounts:detail', pk)
```



```html
<!-- detail.html -->
<a href="{% url 'accounts:follow' user.pk %}">
    {% if request.user in user.followers.all %}
    	UnFollow
    {% else %}
    	Follow
    {% endif %}
</a>
```

