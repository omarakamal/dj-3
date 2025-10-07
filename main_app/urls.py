from django.urls import path
from . import views

urlpatterns = [
    path('quick/',views.quick_route, name='quick_route'),
    path('second/',views.second_route, name='second_route'),
   
]
