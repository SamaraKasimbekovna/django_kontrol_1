from django.urls import path
from .views import *

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),

    path('add/', MovieCreateView.as_view(), name='movie_add'),
    path('edit/<int:pk>/', MovieUpdateView.as_view(), name='movie_edit'),
    path('delete/<int:pk>/', MovieDeleteView.as_view(), name='movie_delete'),

    path('review/<int:pk>/', ReviewCreateView.as_view(), name='add_review'),
]