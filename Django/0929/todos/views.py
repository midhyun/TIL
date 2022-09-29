from django.shortcuts import render, redirect
from todos.models import Todo

# Create your views here.
def index(request):
    todos_ = Todo.objects.all()
    context = {
        'todos':todos_
    }

    return render(request, 'todos/index.html', context)

def create(request):
    content = request.GET.get('content_')
    script = request.GET.get('script')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    completed = request.GET.get('completed')
    Todo.objects.create(
        content=content,
        script=script,
        start_date=start_date,
        end_date=end_date
        )

    return redirect('todos:index')

def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect('todos:index')

def edit(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/edit.html', context)

def modify(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.content = request.GET.get('content_')
    todo.script = request.GET.get('script')
    todo.start_date = request.GET.get('start_date')
    todo.end_date = request.GET.get('end_date')

    todo.save()

    return redirect('todos:index')

def complete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if todo.completed:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()
    
    return redirect('todos:index')