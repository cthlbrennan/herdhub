from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
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
    path('add_calf/', views.add_calf, name='add_calf'),  
    path('view_calf/<int:calf_id>/', views.view_calf, name='view_calf'),  
    path('edit_calf/<int:calf_id>/', views.edit_calf, name='edit_calf'),  
    path('delete_calf/<int:calf_id>/', views.delete_calf, name='delete_calf'),
    path('send_message/', views.send_message, name='send_message'),
    path('404/', views.show404page, name='show_404'),
    path('500/', views.show500page, name='show_500'),
    ]

handler404 = 'herdhub.views.show404page' 
handler500 = 'herdhub.views.show500page'