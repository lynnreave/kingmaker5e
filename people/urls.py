
from django.urls import path
from . import views

urlpatterns = [
    path('', views.people, name='people'),
    path('person/<int:pk>/', views.person_detail, name='person_detail'),
    path('person/new/', views.person_new, name='person_new'),
    path('person/<int:pk>/edit/', views.person_edit, name='person_edit'),
]
