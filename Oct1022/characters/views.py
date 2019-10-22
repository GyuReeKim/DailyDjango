from django.shortcuts import render, redirect
from .forms import BigForm, SmallForm
from .models import Big

# Create your views here.
def index(request):
    bigs = Big.objects.all()
    context = {
        'bigs': bigs
    }
    return render(request, 'characters/index.html', context)

def big_create(request):
    if request.method == "POST":
        form = BigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('characters:index')
    else:
        form = BigForm()
    context = {
        'form': form
    }
    return render(request, 'characters/form.html', context)