from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Articles, Comments
from .forms import ArticleForm, CommentForm
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
            articleform = form.save(commit=False)
            articleform.user = request.user
            articleform.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/forms.html', context)

def detail(request, pk):
    article = Articles.objects.get(pk=pk)
    context = {
        'form': CommentForm(),
        'article': article,
        'comments': article.comments_set.all(),
    }
    return render(request, 'articles/detail.html', context)

@login_required
def update(request, article_pk, pk):
    article = Articles.objects.get(pk=article_pk)
    if request.user.pk == pk:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                articleform = form.save(commit=False)
                articleform.user = request.user
                articleform.save()
                return redirect('articles:index')
        else:
            form = ArticleForm(instance=article)
        context = {
            'form': form
        }
        return render(request, 'articles/forms.html', context)
    else:
        return redirect('accounts:error')

@login_required
def delete(request,article_pk, pk):
    if request.user.pk == pk:
        article = Articles.objects.get(pk=article_pk)
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('acconts:error')

@login_required
def comment(request, pk):
    article = Articles.objects.get(pk=pk)
    com = CommentForm(request.POST)
    if com.is_valid():
        commen = com.save(commit=False)
        commen.article_id = pk
        commen.user = request.user
        commen.save()
    return redirect('articles:detail', pk)

@login_required
def comment_delete(request, article_pk, pk):
    comment = Comments.objects.get(pk=pk)
    comment.delete()
    return redirect('articles:detail', article_pk)