from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/movie_list.html', context)

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    context = {
        'movie': movie,
        }
    return render(request, 'movies/movie_detail.html', context)

def movie_search(request):
    search_term = request.GET.get('search', '')
    movie = Movie.objects.filter(name__icontains=search_term)
    context = {
            'movie': movie,
            }
    html_content = render_to_string('movies/movie_search.html', context)
    return HttpResponse(html_content)

def autocomplete(request):
    search_term = request.GET.get('term', '')
    movies = Movie.objects.filter(name__icontains=search_term)
    suggestions = [movie.name for movie in movies]
    return JsonResponse({'suggestions': suggestions})