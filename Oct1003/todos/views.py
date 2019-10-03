from django.shortcuts import render, redirect
from .models import Todo # 추가

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    due_date = request.GET.get('duedate')

    todo = Todo()
    todo.title = title
    todo.due_date = due_date
    todo.save()

    return redirect('/todos/')

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()

    return redirect('/todos/')

def edit(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo': todo
    }
    
    return render(request, 'edit.html', context)

def update(request, id):
    todo = Todo.objects.get(id=id)

    title = request.GET.get('title')
    due_date = request.GET.get('duedate')

    todo.title = title
    todo.due_date = due_date
    todo.save()

    return redirect('/todos/')