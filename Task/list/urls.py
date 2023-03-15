from django.urls import path
from .views import urls_list

urlpatterns = [
    path('',urls_list,name='urls_list'),
    
]
