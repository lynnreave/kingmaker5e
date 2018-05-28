from django.urls import path
from . import views
from .vars import app_name
app_name = app_name

urlpatterns = [
    path('', views.diplomatic_relations, name='diplomatic_relations'),
    path('diplomatic_relations', views.diplomatic_relations, name='diplomatic_relations'),
    path(
        'diplomatic_relation/new/', views.diplomatic_relation_new, name='diplomatic_relation_new'
    ),
    path(
        'diplomatic_relation/<int:pk>/edit/', views.diplomatic_relation_edit,
        name='diplomatic_relation_edit'
    ),
    path(
        'diplomatic_relation/<int:pk>/delete/', views.diplomatic_relation_delete,
        name='diplomatic_relation_delete'
    ),
]
