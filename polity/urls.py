from django.urls import path
from . import views
from .vars import app_name
app_name = app_name

urlpatterns = [
    path('', views.polities, name='polities'),
    path('polities', views.polities, name='polities'),
    path('polity/new/', views.polity_new, name='polity_new'),
    path('polity/<int:pk>/edit/', views.polity_edit, name='polity_edit'),
    path('polity/<int:pk>/delete/', views.polity_delete, name='polity_delete'),
]
