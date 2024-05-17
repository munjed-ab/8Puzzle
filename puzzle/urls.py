
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shuffle', views.shuffle, name='shuffle'),
    path('move', views.move, name='move'),
    path('solve', views.solve, name='solve'),
]