from django.shortcuts import render, redirect

from movie_review.models import Review
from .forms import ReviewForm
# from .models import Review

# Create your views here.
def index(request):
    review_list = Review.objects.order_by('pk')
    context = {
        'review_list' : review_list,
    }
    return render(request, 'movie_review/index.html', context)

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

def detail(request,pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review':review,
    }
    return render(request, 'movie_review/detail.html', context)

def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('movie_review:index')
    context = {
        'review':review
    }
    return render(request, 'movie_review/detail.html', context)

