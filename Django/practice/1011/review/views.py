from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review

# Create your views here.
def index(request):
    review = Review.objects.all()
    context = {
        'review': review
    }
    return render(request, 'review/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('review:index')
    else:
        form = ReviewForm()
    context ={
        'form':form
    }
    return render(request, 'review/create.html', context)

def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review:detail', pk)
    else:
        form = ReviewForm(instance=review)
    context ={
        'form':form
    }
    return render(request, 'review/create.html', context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review':review
    }
    return render(request, 'review/detail.html', context)

def delete(reuqest, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('review:index')