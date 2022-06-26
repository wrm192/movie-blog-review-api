from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from movie import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:pk>/', views.movie_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
