from django.urls import path
from . import views
from .vars import app_name
app_name = app_name

urlpatterns = [
    path('', views.events, name='events'),
    path('events', views.events, name='events'),
    path('event/new/', views.event_new, name='event_new'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),
]
