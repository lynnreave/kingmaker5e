"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page': 'core:home'}, name='logout'),
    path('admin/', admin.site.urls),
    path('armed_forces/', include('armed_forces.urls')),
    path('diplomacy/', include('diplomacy.urls')),
    path('events/', include('events.urls')),
    path('factions/', include('factions.urls')),
    path('festivals/', include('festivals.urls')),
    path('polity/', include('polity.urls')),
    path('people/', include('people.urls')),
    path('settlements/', include('settlements.urls')),
    path('territory/', include('territory.urls')),
    path('trade/', include('trade.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
