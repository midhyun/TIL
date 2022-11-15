from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Articles, Comments
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article_form = form.save(commit=False)
            article_form.user = request.user
            article_form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/forms.html', context)

@login_required
def update(request, pk):
    article = Articles.objects.get(pk=pk)
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

def detail(request, pk):
    article = Articles.objects.get(pk=pk)
    form = CommentForm()
    context = {
        'form':form,
        'article': article
    }
    return render(request, 'articles/detail.html', context)

@login_required
def delete(request, article_pk, pk):
    article = Articles.objects.get(pk=pk)
    article.delete()
    return redirect('articels:index')

@login_required
def comments(request, article_pk):
    article = Articles.objects.get(pk=article_pk)
    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('articles:detail', article_pk)

def delete_comments(request, article_pk, pk):
    comment = Comments.objects.get(pk=pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
