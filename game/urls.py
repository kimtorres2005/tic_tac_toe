from django.urls import path
from .views import home, game, play_game

urlpatterns = [
    path('', home, name='home'),           # Home page
    path('start_game/', game, name='game'),  # Start game page
    path('play_game/', play_game, name='play_game'),  # Play game page
]
