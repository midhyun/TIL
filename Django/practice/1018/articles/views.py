from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Articles, Comment

# Create your views here.
def index(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)

def detail(request, pk):
    article = Articles.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comments': article.comment_set.all(),
        'comment_form': comment_form
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Articles.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)

def delete(request, pk):
    article = Articles.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def comments(request, pk):
    article = Articles.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment_form = form.save(commit=False)
        comment_form.article = article
        comment_form.save()
    return redirect('articles:detail', article.pk)

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
