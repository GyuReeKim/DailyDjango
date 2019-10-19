from django.shortcuts import render, redirect, get_object_or_404
from .forms import CoffeeForm, FlavorForm
from .models import Coffee, Flavor

# Create your views here.
def index(request):
    coffees = Coffee.objects.all()
    context = {
        'coffees': coffees,
    }
    return render(request, 'students/index.html', context)

def create(request):
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:index')
    else:
        form = CoffeeForm()
    context = {
        'form': form,
    }
    return render(request, 'students/form.html', context)

def detail(request, id):
    coffee = get_object_or_404(Coffee, id=id)
    form = FlavorForm()
    context = {
        'coffee': coffee,
        'form': form,
    }
    return render(request, 'students/detail.html', context)

def update(request, id):
    coffee = get_object_or_404(Coffee, id=id)
    if request.method == "POST":
        form = CoffeeForm(request.POST, instance=coffee)
        form.save()
        return redirect('students:detail', id)
    else:
        form = CoffeeForm(instance=coffee)
    context = {
        'form': form,
    }
    return render(request, 'students/form.html', context)

def delete(request, id):
    coffee = get_object_or_404(Coffee, id=id)
    if request.method == "POST":
        coffee.delete()
        return redirect('students:index')

def flavor_create(request, id):
    coffee = get_object_or_404(Coffee, id=id)
    if request.method == "POST":
        form = FlavorForm(request.POST)
        flavor = form.save(commit=False)
        flavor.coffee = coffee
        flavor.save()
        return redirect('students:detail', id)
    else:
        pass

def flavor_delete(request, coffee_id, flavor_id):
    flavor = get_object_or_404(Flavor, id=flavor_id)
    if request.method == "POST":
        flavor.delete()
        return redirect('students:detail', coffee_id)
