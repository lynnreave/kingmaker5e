
from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('', views.people, name='people'),
    path('person/new/', views.person_new, name='person_new'),
    path('person/<int:pk>/edit/', views.person_edit, name='person_edit'),
    path('person/<int:pk>/delete/', views.person_delete, name='person_delete'),
    path('noble_ranks', views.noble_ranks, name='noble_ranks'),
    path('noble_rank/new/', views.noble_rank_new, name='noble_rank_new'),
    path('noble_rank/<int:pk>/edit/', views.noble_rank_edit, name='noble_rank_edit'),
    path('noble_rank/<int:pk>/delete/', views.noble_rank_delete, name='noble_rank_delete'),
]
