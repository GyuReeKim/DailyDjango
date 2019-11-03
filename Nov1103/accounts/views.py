from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/form.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/form.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('posts:index')

def user_list(request):
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})

def user_page(request, user_id):
    user_info = get_object_or_404(User, id=user_id)
    return render(request, 'accounts/user_page.html', {'user_info': user_info})

def follow(request, user_id):
    you = get_object_or_404(User, id=user_id)
    me = request.user
    
    if you != me:
        if me in you.followers.all():
            you.followers.remove(me)
        else:
            you.followers.add(me)
    return redirect('accounts:user_page', user_id)

def delete(request, user_id):
    user_info = get_object_or_404(User, id=user_id)
    user = request.user

    if user == user_info:
        user.delete()
    return redirect('posts:index')

def update(request, user_id):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:user_page', user_id)
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/form.html', {'form': form})

def password(request, user_id):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:user_page', user_id)
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/form.html', {'form': form})