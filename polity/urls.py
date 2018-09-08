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
    path('polity/<int:pk>/details/', views.polity_details, name='polity_details'),
    path(
        'polity/<int:pk>/modify_treasury/<str:dir><int:step>',
        views.polity_modify_treasury, name='polity_modify_treasury'
    ),
    path(
        'polity/<int:pk>/modify_unrest/<str:dir><int:step>',
        views.polity_modify_unrest, name='polity_modify_unrest'
    ),
    path('polity/<int:polity_id>/logs/<int:current_year>', views.logs, name='logs'),
    path('polity/<int:polity_id>/logs/add_year', views.logs_add_year, name='logs_add_year'),
    path(
        'polity/<int:polity_id>/logs/<int:current_year>/log_entry/<int:pk>/edit/',
        views.log_entry_edit, name='log_entry_edit'
    ),
]
