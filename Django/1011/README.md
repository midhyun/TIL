# TIL Project-Template

## INTRO

## ![img1](README.assets/img1.gif)

- 🗓 프로젝트 기간
  - 2022.10.11
- 💻 사용 기술
  - Python, Django, HTML, CSS, Bootstrap5
- ⭐ 나의 역할
  - `driver`  : movie_reivew, `Model`작성 , `Create` 기능 구현
  - `navigator` : movie_reivew `Create` 및 `Update`파일 업로드 기능 추가, 추가된 이미지는 최대 1개이며, 디테일에 표시되도록 함.
- 💡 배운 점
  - CRUD 모델 폼의 기능에 익숙해 질 수 있었음.
  - 추가로 파일을 업로드함으로써 서버에 파일이 업로드되고, 업로드된 파일이 게시글에 나타날 수 있도록 구현하는데 db에는 파일의 경로가 저장 됨을 알 수 있었음.
  - 앞으로 여러파일을 업로드 하는 법도 학습해야 겠음.



## 🚩목적

> project's goal

- Movie_Reivew CRUD기능이 있는 게시판 구현
- 추가적인 작업 (개인적으로)



# 🧾기능 소개

- Nav_bar 의 리뷰작성 버튼으로 리뷰를 작성 할 수 있음
  - 제목, 내용, 영화제목, 점수와 영화 포스터를 첨부 할 수 있음
- detail 페이지에는 작성한 내용이 표시되며, 업로드한 영화 포스터가 상단에 나타남
- 수정시 에는 이미지의 경로를 지울 수 있으나 새로운 이미지를 업로드하기 위해서는 지운 뒤 다시 수정탭에 들어가서 업로드 해야 함. 한번에 한가지 작업만 수행 가능함.

# 문제 해결

## 문제 상황

- Model_Form 에 파일을 업로드하는 프론트가 구현되었으나 실제로 업로드를 하면 서버에 이미지가 넘어가지 않음.
- DB에도 이미지의 경로가 표시되지 않음
- admin에서 파일을 추가 할 경우 정상적으로 업로드 됨

- 수정시에 경로 제거는 되었으나, 새로 추가 되지 않음.

## 해결

- 파일업로드의 경우 request.POST에 담기지 않고 request.FILES 로 추가로 넘겨주어야 했음.

```python
def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review_form.save()
            return redirect('movie_review:index')
    else:
        review_form = ReviewForm()
    context = {
        'review_form' : review_form,
    }
    return render(request, 'movie_review/form.html', context=context)
```

- 수정시에도 마찬가지로 request.FILES로 추가로 넘겨주는 동작이 필요했음. instance=request.objects.get(pk=pk) 로는 같이 넘어가지 않음

```python
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('movie_review:detail', review.pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {
        'review_form' : review_form,
    }
    return render(request, 'movie_review/form.html', context)
```

