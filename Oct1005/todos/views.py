from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')
        due_date = request.POST.get('due-date')

        todo = Todo.objects.create(
            title=title,
            author=author,
            content=content,
            due_date=due_date,
        )
        return redirect('todos:index')
    else:
        return render(request, 'create.html')

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todos:index')

def update(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')
        due_date = request.POST.get('due-date')

        todo.title = title
        todo.author = author
        todo.content = content
        todo.due_date = due_date
        todo.save()
        return redirect('todos:detail', todo.id)
    else:
        context = {
            'todo': todo,
        }
        return render(request, 'update.html', context)

def detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo,
    }
    return render(request, 'detail.html', context)