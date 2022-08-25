# 데이터베이스 07 - ORM

<aside>
💡 코드를 작성한 실습 파일을 압축해서 실라버스에 제출해주세요.

</aside>

### 1. `db/models.py` 파일에 아래의 모델 2개 `Director` `Genre` 를 작성하세요.

> 기본 코드
> 

```python
class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()
```

### 2. 모델을 마이그레이트(migrate) 하세요.

```bash
# 가상환경 실행 확인 후 아래 명령어를 터미널에 입력합니다.
python manage.py makemigrations

python manage.py migrate
```

### 3. Queryset 메소드 `create` 를 활용해서  `Director` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| name | debut | country |
| --- | --- | --- |
| 봉준호 | 1993-01-01 | KOR |
| 김한민 | 1999-01-01 | KOR |
| 최동훈 | 2004-01-01 | KOR |
| 이정재 | 2022-01-01 | KOR |
| 이경규 | 1992-01-01 | KOR |
| 한재림 | 2005-01-01 | KOR |
| Joseph Kosinski | 1999-01-01 | KOR |
| 김철수 | 2022-01-01 | KOR |

> 코드 작성
> 

```python
lst = (""" 봉준호 | 1993-01-01 | KOR 
 김한민 | 1999-01-01 | KOR 
 최동훈 | 2004-01-01 | KOR 
 이정재 | 2022-01-01 | KOR 
 이경규 | 1992-01-01 | KOR 
 한재림 | 2005-01-01 | KOR 
 Joseph Kosinski | 1999-01-01 | KOR 
 김철수 | 2022-01-01 | KOR """).split('\n')
result = []
for i in lst:
    a = i.split('|')
    result.append(a)
answ = []
for i in result:
    name_, debut_, country_ = i[0].strip(), i[1].strip(), i[2].strip()
    Director.objects.create(name= name_, debut= debut_, country= country_)
```

### 4. `인스턴스 조작` 을 활용하여`Genre` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| title |
| --- |
| 액션 |
| 드라마 |
| 사극 |
| 범죄 |
| 스릴러 |
| SF |
| 무협 |
| 첩보 |
| 재난 |

> 코드 작성
> 

```python
lst = ('''액션
드라마
사극
범죄
스릴러
SF
무협
첩보
재난''').split('\n')

for i in lst:
    genre = Genre()
    genre.title = i
    genre.save()
```

### 5. Queryset 메소드 `all` 을 활용해서 `Director` 테이블의 모든 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
Joseph Kosinski 1999-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
# 1
lst = Director.objects.all()

for object in lst:
    print(object.name, object.debut, object.country)
# 2 
for object in lst.values():
    print(object['name'], object['debut'], object['country'])
```

### 6. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `id` 가 1인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
columns = ['name','debut','country']
dic_ = Director.objects.values().get(id = 1)
for i in columns:
    print(dic_[i],end=' ')
```

### 7. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 USA인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성
> 

```python
Director.objects.get(country = 'USA')
```

### 8. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지
> 

```bash
DoesNotExist: Director matching query does not exist.
```

> 이유 작성
> 

```
.get() 메소드를 사용했을 때 값이 0이거나 1초과 일 경우, 즉 1이 아닐 경우 에러를 발생합니다.
```

### 9. Queryset 메소드 `get` 과 `save` 를 활용해서 `Director` 테이블에서  `name` 이 Joseph Kosinski인 데이터를 조회해서 `country` 를 USA 로 수정하고, 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
Joseph Kosinski 1999-01-01 00:00:00 USA
```

> 코드 작성
> 

```python
a = Director.objects.get(name = 'Joseph Kosinski')
a.country = 'USA'
a.save()
print(a.name, a.debut, a.country)
```

### 10. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성
> 

```python
Director.objects.get(country = 'KOR')
```

### 11. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지
> 

```bash
MultipleObjectsReturned: get() returned more than one Director -- it returned 7!
```

> 이유 작성
> 

```
.get() 메소드로 반환되는 값이 1개가 아닐 경우 오류가 발생함 KOR 은 7개임.
```

### 12. Queryset 메소드 `filter` 를 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
lst = Director.objects.filter(country='KOR')

for i in lst:
    print(i.name, i.debut, i.country)
```

### 13. 본인이 생각하는 혹은 찾은 `get` 과 `filter` 의 차이를 작성하세요.

```
.get 은 pk로 값을 찾고자 할 때 사용해야 한다. 의외의 경우 에러를 발생시킨다.(try-except)
.filter 는 중복된 값들 혹은 값이 존재하지 않을 경우, 리스트로 반환될 수 있다.
```

### 14. Queryset 메소드 `get` 과 `delete`를 활용해서  `Director` 테이블에서 `name` 이 김철수인 데이터를 삭제하는 코드를 작성하세요.

> 코드 작성
> 

```python
Director.objects.get(name='김철수').delete()
```