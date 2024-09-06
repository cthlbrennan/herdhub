from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_cow', views.add_cow, name='add_cow'),
    path('view_cow/<int:cow_id>/', views.view_cow, name='view_cow'),
    path('edit_cow/<int:cow_id>/', views.edit_cow, name='edit_cow'),
    path('delete_cow/<int:cow_id>/', views.delete_cow, name='delete_cow'),
    path('add_bull/', views.add_bull, name='add_bull'),
    path('view_bull/<int:bull_id>/', views.view_bull, name='view_bull'),
    path('edit_bull/<int:bull_id>/', views.edit_bull, name='edit_bull'),
    path('delete_bull/<int:bull_id>/', views.delete_bull, name='delete_bull'),
    path('add_breeding_event/', views.add_breeding_event, name='add_breeding_event'),  
    path('view_breeding/<int:breeding_id>/', views.view_breeding, name='view_breeding'),  
    path('edit_breeding/<int:breeding_id>/', views.edit_breeding, name='edit_breeding'),  
    path('delete_breeding/<int:breeding_id>/', views.delete_breeding, name='delete_breeding'),

    ]