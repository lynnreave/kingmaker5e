from django.urls import path
from . import views
from .vars import app_name
app_name = app_name

urlpatterns = [
    path('', views.factions, name='factions'),
    path('factions', views.factions, name='factions'),
    path('faction/new/', views.faction_new, name='faction_new'),
    path('faction/<int:pk>/edit/', views.faction_edit, name='faction_edit'),
    path('faction/<int:pk>/delete/', views.faction_delete, name='faction_delete'),
]
