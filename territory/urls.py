from django.urls import path
from . import views
from .vars import app_name
app_name = app_name

urlpatterns = [
    path('', views.territories, name='territories'),
    path('territories', views.territories, name='territories'),
    path('territory/new/', views.territory_new, name='territory_new'),
    path('territory/<int:pk>/edit/', views.territory_edit, name='territory_edit'),
    path('territory/<int:pk>/delete/', views.territory_delete, name='territory_delete'),
    path('types', views.types, name='types'),
    path('type/new/', views.type_new, name='type_new'),
    path('type/<int:pk>/edit/', views.type_edit, name='type_edit'),
    path('type/<int:pk>/delete/', views.type_delete, name='type_delete'),
    path('features', views.features, name='features'),
    path('feature/new/', views.feature_new, name='feature_new'),
    path('feature/<int:pk>/edit/', views.feature_edit, name='feature_edit'),
    path('feature/<int:pk>/delete/', views.feature_delete, name='feature_delete'),
    path('improvements', views.improvements, name='improvements'),
    path('improvement/new/', views.improvement_new, name='improvement_new'),
    path('improvement/<int:pk>/edit/', views.improvement_edit, name='improvement_edit'),
    path('improvement/<int:pk>/delete/', views.improvement_delete, name='improvement_delete'),
    path('maps', views.maps, name='maps'),
    path('map/<int:pk>/', views.map, name='map'),
    path('map/new/', views.map_new, name='map_new'),
    path('map/<int:pk>/edit/', views.map_edit, name='map_edit'),
]
