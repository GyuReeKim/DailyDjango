from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm
from .models import Question

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'questions/index.html', context)

def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('questions:index')
    else:
        form = QuestionForm()
    context = {
        'form': form,
    }
    return render(request, 'questions/form.html', context)

def detail(request, id):
    question = get_object_or_404(Question, id=id)
    context = {
        'question': question,
    }
    return render(request, 'questions/detail.html', context)