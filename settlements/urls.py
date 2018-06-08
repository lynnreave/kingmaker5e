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
        'settlement/<int:settlement_id>/details/', views.buildings, name='buildings'
    ),
    path(
        'settlement/<int:settlement_id>/building/new', views.building_new, name='building_new'
    ),
    path(
        'settlement/<int:settlement_id>/building/<int:pk>/edit', views.building_edit,
        name='building_edit'
    ),
    path(
        'settlement/<int:settlement_id>/building/<int:pk>/delete', views.building_delete,
        name='building_delete'
    ),
    path(
        'settlement/<int:settlement_id>/districts', views.districts, name='districts'
    ),
    path(
        'settlement/<int:settlement_id>/districts/new', views.district_new, name='district_new'
    ),
    path(
        'settlement/<int:settlement_id>/districts/<int:pk>/edit', views.district_edit,
        name='district_edit'
    ),
    path(
        'settlement/<int:settlement_id>/districts/<int:pk>/delete', views.district_delete,
        name='district_delete'
    ),
    path(
        'settlement/<int:settlement_id>/districts/<int:district_id>/lots', views.lots, name='lots'
    ),
    path(
        'settlement/<int:settlement_id>/districts/<int:district_id>/lots/new',
        views.lot_new, name='lot_new'
    ),
    path(
        'settlement/<int:settlement_id>/districts/<int:district_id>/lots/<int:pk>/edit',
        views.lot_edit, name='lot_edit'
    ),
    path(
        'settlement/<int:settlement_id>/districts/<int:district_id>/lots/<int:pk>/delete',
        views.lot_delete, name='lot_delete'
    ),
    path('strongholds', views.strongholds, name='strongholds'),
    path('stronghold/new/', views.stronghold_new, name='stronghold_new'),
    path('stronghold/<int:pk>/edit/', views.stronghold_edit, name='stronghold_edit'),
    path('stronghold/<int:pk>/delete/', views.stronghold_delete, name='stronghold_delete'),
    path(
        'stronghold/<int:stronghold_id>/details/', views.expansions, name='expansions'
    ),
    path(
        'stronghold/<int:stronghold_id>/expansion/new', views.expansion_new, name='expansion_new'
    ),
    path(
        'stronghold/<int:stronghold_id>/expansion/<int:pk>/edit', views.expansion_edit,
        name='expansion_edit'
    ),
    path(
        'stronghold/<int:stronghold_id>/expansion/<int:pk>/delete', views.expansion_delete,
        name='expansion_delete'
    ),
]
