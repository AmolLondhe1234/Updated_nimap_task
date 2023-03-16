from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def urls_list(reuest):
    list={
        'UserRegister':'api/register/',
        'ClientListCreate':'api/clients/',
        'ClientDetails':'api/clients/id/',
        'ProjectCreate':'api/clients/id/project',
        'ProjectListLoggedIn-User':'api/projects',
    }
    return Response(list)
    