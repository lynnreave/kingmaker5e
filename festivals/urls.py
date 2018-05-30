from django.urls import path
from . import views
from .vars import app_name
app_name = app_name

urlpatterns = [
    path('', views.festivals, name='festivals'),
    path('festivals', views.festivals, name='festivals'),
    path('festival/new/', views.festival_new, name='festival_new'),
    path('festival/<int:pk>/edit/', views.festival_edit, name='festival_edit'),
    path('festival/<int:pk>/delete/', views.festival_delete, name='festival_delete'),
]
