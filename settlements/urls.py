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
    path(
        'settlement/<int:settlement_id>/details/', views.buildings, name='settlement_details'
    ),
    path(
        'settlement/<int:settlement_id>/add_building/', views.building_new, name='building_new'
    ),
    path(
        'settlement/<int:settlement_id>/building/<int:pk>/edit', views.building_edit,
        name='building_edit'
    ),
    path(
        'settlement/<int:settlement_id>/building/<int:pk>/delete', views.building_delete,
        name='building_delete'
    ),
]
