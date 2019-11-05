from django.shortcuts import render
from .models import One, Two

# Create your views here.
def index(request):
    return render(request, 'infos/index.html')

def one_list(request):
    numbers = One.objects.all()
    context = {
        'numbers': numbers,
        'pick': 'one',
    }
    return render(request, 'infos/number_list.html', context)

def two_list(request):
    numbers = Two.objects.all()
    context = {
        'numbers': numbers,
        'pick': 'two',
    }
    return render(request, 'infos/number_list.html', context)