from django.shortcuts import render, redirect, get_object_or_404
from .forms import CharacterForm
from .models import Character

# Create your views here.
def index(request):
    characters = Character.objects.all()
    context = {
        'characters': characters,
    }
    return render(request, 'characters/index.html', context)

def create(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user
            character.save()
            return redirect('characters:index')
    else:
        form = CharacterForm()
    context = {
        'form': form,
    }
    return render(request, 'characters/form.html', context)

def detail(request, id):
    character = get_object_or_404(Character, id=id)
    context = {
        'character': character,
    }
    return render(request, 'characters/detail.html', context)

def like(request, id):
    character = get_object_or_404(Character, id=id)
    current_user = request.user
    if character != current_user:
        if current_user in character.like_users.all():
            character.like_users.remove(current_user)
        else:
            character.like_users.add(current_user)
    return redirect('characters:detail', id)