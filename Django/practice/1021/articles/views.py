from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Review.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/forms.html', context)

@login_required
def update(request, pk):
    article = Review.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            form = ArticleForm(instance=article)
        context = {
            'form': form
        }
        return render(request, 'articles/forms.html', context)
    else:
        return redirect('articles:error')

@login_required
def delete(request, pk):
    article = Review.objects.get(pk=pk)
    if request.user.pk == article.user.pk:
        Review.objects.get(pk=pk).delete()
        return redirect('articles:index')
    else:
        return redirect('articles:error')

def detail(request, pk):
    article = Review.objects.get(pk=pk)
    form = CommentForm()
    context = {
        'form': form,
        'article': article
    }
    return render(request, 'articles/detail.html', context)

@login_required
def comments(request, article_pk):
    article = Review.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            print(-1)
            temp = form.save(commit=False)
            temp.review = article
            temp.user = request.user
            temp.save()
            return redirect('articles:detail', article.pk)

@login_required
def comments_delete(request, article_pk, pk):
    comment = Comment.objects.get(pk=pk)
    if comment.user == request.user:
        comment.delete()
        return redirect('articles:detail', article_pk)
    else:
        return redirect('articles:error')

def error(request):
    return render(request, 'articles/error.html')