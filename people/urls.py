from django.urls import path
from . import views
from .vars import app_name
app_name = app_name

urlpatterns = [
    path('', views.people, name='people'),
    path('people', views.people, name='people'),
    path('person/new/', views.person_new, name='person_new'),
    path('person/<int:pk>/edit/', views.person_edit, name='person_edit'),
    path('person/<int:pk>/delete/', views.person_delete, name='person_delete'),
    path('noble_ranks', views.noble_ranks, name='noble_ranks'),
    path('noble_rank/new/', views.noble_rank_new, name='noble_rank_new'),
    path('noble_rank/<int:pk>/edit/', views.noble_rank_edit, name='noble_rank_edit'),
    path('noble_rank/<int:pk>/delete/', views.noble_rank_delete, name='noble_rank_delete'),
    path('awards', views.awards, name='awards'),
    path('award/new/', views.award_new, name='award_new'),
    path('award/<int:pk>/edit/', views.award_edit, name='award_edit'),
    path('award/<int:pk>/delete/', views.award_delete, name='award_delete'),
]
