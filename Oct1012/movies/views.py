from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        title_en = request.POST.get('title-en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open-date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch-grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster-url')
        description = request.POST.get('description')

        movie = Movie.objects.create(
            title=title,
            title_en=title_en,
            audience=audience,
            open_date=open_date,
            genre=genre,
            watch_grade=watch_grade,
            score=score,
            poster_url=poster_url,
            description=description,
        )
        return redirect('movies:index')
    else:
        return render(request, 'create.html')

def detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'detail.html')

def update(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == "POST":
        title = request.POST.get('title')
        title_en = request.POST.get('title-en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open-date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch-grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster-url')
        description = request.POST.get('description')

        movie.title = title
        movie.title_en = title_en
        movie.audience = audience
        movie.open_date = open_date
        movie.genre = genre
        movie.watch_grade = watch_grade
        movie.score = score
        movie.poster_url = poster_url
        movie.description = description

        movie.save()
        return redirect('movies:detail', movie.id)
    else:
        context = {
            'movie': movie,
        }
        return render(request, 'update.html', context)

def delete(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('movies:index')