from django.shortcuts import render
from django.http import HttpResponse
import requests
import urllib.request
from .models import Film


#Passwords
#baltimore

def __saveFilm(info):
    posterLocalName = info['nameOriginal'] + info['posterUrl'][-4:]
    urllib.request.urlretrieve(info['posterUrl'], 'crimsonFilms/static/crimsonFilms/posters/' + posterLocalName)
    newFilm = Film(
        titleO=info['nameOriginal'],
        titleEn=info['nameEn'] if info['nameEn'] != None else info['nameOriginal'],
        titleRu=info['nameRu'] if info['nameRu'] != None else info['nameOriginal'],
        kID=info['kinopoiskId'],
        imdbID=info['imdbId'],
        poster=info['posterUrl'],
        posterLocal=posterLocalName
    )
    newFilm.save()
    return newFilm


def __searchKino(keyword=None, page=1):
    keywordR = ''
    if keyword != None:
        keywordR = "keyword=" + keyword + '&'
    api_url = "https://kinopoiskapiunofficial.tech/api/v2.2/films?order=RATING&type=ALL&ratingFrom=0&ratingTo=10&yearFrom=1000&yearTo=3000&" + keywordR + "page=" + str(
        page)
    headers = {
        'X-API-KEY': '38e4b93a-b881-46ca-b7af-2d43b455cef8',
        'Content-Type': 'application/json'
    }
    response = requests.get(api_url, headers=headers).json()
    return response["items"]


def welcomePage(request):
    return render(request, 'crimsonFilms/home.html')


def filmPage(request):
    requestImdbID = request.GET['imdbID']
    film = None
    if Film.objects.filter(imdbID=requestImdbID).exists():
        film = Film.objects.filter(imdbID=requestImdbID).first()
    else:
        api_url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films?order=RATING&type=ALL&ratingFrom=0&ratingTo=10&yearFrom=1000&yearTo=3000&imdbId=' + requestImdbID + '&page=1'
        headers = {
            'X-API-KEY': '38e4b93a-b881-46ca-b7af-2d43b455cef8',
            'Content-Type': 'application/json'
        }
        response = requests.get(api_url, headers=headers).json()
        if (response['total'] > 0):
            film = __saveFilm(response['items'][0])

    context = {
        'title': 'Film',
        'film': film
    }
    return render(request, 'crimsonFilms/film.html', context)


def catalog(request):
    filmsWatch = Film.objects.exclude(videoLocal='')
    context = {
        'title': 'Catalog',
        'filmsWatch': filmsWatch
    }
    if (request.GET.get('search')):
        context['films'] = __searchKino(request.GET['search'])
    return render(request, 'crimsonFilms/catalog.html', context)


def experiment(request):
    return render(request, 'crimsonFilms/expVideo.html')
