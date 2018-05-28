from django.urls import path
from . import views
from .vars import app_name
app_name = app_name

urlpatterns = [
    path('', views.settlements, name='settlements'),
    path('settlements', views.settlements, name='settlements'),
    path('settlement/new/', views.settlement_new, name='settlement_new'),
    path('settlement/<int:pk>/edit/', views.settlement_edit, name='settlement_edit'),
    path('settlement/<int:pk>/delete/', views.settlement_delete, name='settlement_delete'),
]
