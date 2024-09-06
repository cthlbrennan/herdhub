from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_cow', views.add_cow, name='add_cow'),
    path('view_cow/<int:cow_id>/', views.view_cow, name='view_cow'),
    path('edit_cow/<int:cow_id>/', views.edit_cow, name='edit_cow'),
    path('delete_cow/<int:cow_id>/', views.delete_cow, name='delete_cow'),
]