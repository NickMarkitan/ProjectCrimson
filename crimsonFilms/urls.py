from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.catalog, name='films-catalog'),
    path('', views.welcomePage, name='films-welcome'),
    path('film/', views.filmPage, name='films-film'),
    path('experiment/', views.experiment, name="films-experiment")
]