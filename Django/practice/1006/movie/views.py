from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movie = Movie.objects.order_by('-pk')
    context = {
        'movie': movie
    }
    return render(request, 'movie/index.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie':movie
    }
    return render(request, 'movie/detail.html', context)

def create(request):
    if request.method =='POST':
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('movie:index')
    else:
        movie_form = MovieForm()
    context = {
        'movie_form': movie_form
    }
    return render(request, 'movie/create.html', context)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('movie:detail', movie.pk)
    else:
        movie_form = MovieForm(instance=movie)
    context = {
        'movie_form': movie_form
    }
    return render(request, 'movie/update.html', context)

def delete(reqeust, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movie:index')