from django.urls import path
from . import views
from .vars import app_name
app_name = app_name

urlpatterns = [
    path('', views.armies, name='armies'),
    path('armies', views.armies, name='armies'),
    path('army/new/', views.army_new, name='army_new'),
    path('army/<int:pk>/edit/', views.army_edit, name='army_edit'),
    path('army/<int:pk>/delete/', views.army_delete, name='army_delete'),
]
