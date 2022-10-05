from django.shortcuts import render, redirect
from .forms import CrudForm
from .models import Crud
# Create your views here.
def index(request):
    crud = Crud.objects.all()
    context = {
        'crud':crud
    }
    return render(request, 'crud/index.html', context )

def create(request):
    if request.method == 'POST':
        crud_form = CrudForm(request.POST)
        if crud_form.is_valid():
            crud_form.save()
            return redirect('crud:index')
    else:
        crud_form = CrudForm()
    context = {
        'crud_form': crud_form,
    }
    return render(request, 'crud/create.html', context)

def detail(request, pk):
    crud = Crud.objects.get(pk=pk)
    context = {
        'crud':crud
    }
    return render(request, 'crud/detail.html', context)

def update(request, pk):
    crud = Crud.objects.get(pk=pk)
    if request.method == 'POST':
        crud_form = CrudForm(request.POST, instance=crud)
        if crud_form.is_valid():
            crud_form.save()
            return redirect('crud:detail', crud.pk)
    else:
        crud_form = CrudForm(instance=crud)
    context = {
        'crud_form': crud_form,
    }
    return render(request, 'crud/update.html', context)


def delete(request, pk):
    crud = Crud.objects.get(pk=pk)
    crud.delete()

    return redirect('crud:index')