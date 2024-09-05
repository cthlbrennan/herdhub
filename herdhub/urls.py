from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_cow', views.add_cow, name='add_cow'),
    path('view_cow/<int:cow_id>/', views.view_cow, name='view_cow'),
]