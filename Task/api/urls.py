from django.urls import path
from .views import ClientList,ClientDetails,ProjectCreate,ProjectList,UserRegister

urlpatterns = [
    path('clients/', ClientList.as_view()),
    path('clients/<int:pk>/',ClientDetails.as_view()),
    path('clients/<int:pk>/project',ProjectCreate.as_view()),
    path('projects/',ProjectList.as_view()),
    path('register/',UserRegister.as_view())
    
    
]
