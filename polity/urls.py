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
    path('log_entries', views.log_entries, name='log_entries'),
    path('log_entry/new/', views.log_entry_new, name='log_entry_new'),
    path('log_entry/<int:pk>/edit/', views.log_entry_edit, name='log_entry_edit'),
]
