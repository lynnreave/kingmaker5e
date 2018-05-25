from django.urls import path
from . import views

app_name = 'territory'

urlpatterns = [
    path('', views.territories, name='territories'),
    path('territories', views.territories, name='territories'),
    path('types', views.types, name='types'),
    path('features', views.features, name='features'),
    path('improvements', views.improvements, name='improvements'),
]