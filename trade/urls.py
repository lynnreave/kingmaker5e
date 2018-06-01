from django.urls import path
from . import views
from .vars import app_name
app_name = app_name

urlpatterns = [
    path('', views.trade_routes, name='trade_routes'),
    path('trade_routes', views.trade_routes, name='trade_routes'),
    path('trade_route/new/', views.trade_route_new, name='trade_route_new'),
    path('trade_route/<int:pk>/edit/', views.trade_route_edit, name='trade_route_edit'),
    path('trade_route/<int:pk>/delete/', views.trade_route_delete, name='trade_route_delete'),
    path('trade_route/<int:pk>/activate/', views.trade_route_activate, name='trade_route_activate'),
    path(
        'trade_route/<int:pk>/deactivate/', views.trade_route_deactivate, name='trade_route_deactivate'
    ),
]
