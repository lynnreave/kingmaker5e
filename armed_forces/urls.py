from django.urls import path
from . import views
from .vars import app_name
app_name = app_name

urlpatterns = [
    path('', views.armed_forces, name='armed_forces'),
    path('armed_forces', views.armed_forces, name='armed_forces'),
    path('armed_force/new/', views.armed_force_new, name='armed_force_new'),
    path('armed_force/<int:pk>/edit/', views.armed_force_edit, name='armed_force_edit'),
    path('armed_force/<int:pk>/delete/', views.armed_force_delete, name='armed_force_delete'),
]
