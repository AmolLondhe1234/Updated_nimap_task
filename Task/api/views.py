
from datetime import timezone
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Client,Project
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_201_CREATED,HTTP_404_NOT_FOUND
from .serializer import ClientSerializer,ProjectSerializer,ClientDSerializer,UserSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from django.contrib.auth.models import User

class UserRegister(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    authentication_classes=[BasicAuthentication]

class ClientList(generics.ListCreateAPIView):
    authentication_classes=[BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)
    # def post(self, request, format=None):
    #     serializer = ClientSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(self.request['created_by']=)
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
    
class ClientDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientDSerializer
    
    
    def perform_update(self, serializer):
        serializer.save(updated_at=timezone)
        
        
class ProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)        
    
    

class ProjectCreate(generics.CreateAPIView):
    def perform_create(self, serializer):
        client_id=self.kwargs['pk']
        client=Client.objects.get(id=client_id)
        serializer.save(client=client)
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer    
        
    # def get(self,request):
    #     project=Project.objects.all()
    #     serializer=ProjectSerializer(project, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request, pk):
    #     try:
    #         client = Client.objects.get(id=pk)
    #         # users= User.objects.all()
    #     except Client.DoesNotExist:
    #         return Response(status=HTTP_404_NOT_FOUND)
    #     data=request.data.copy()
    #     serializer = ProjectSerializer(data=data)
    #     usernames = data.pop('username', None)
    #     if serializer.is_valid():
    #         project=serializer.save(client=client)
    #         if usernames is not None:
    #             users = User.objects.filter(username__in=usernames)
    #             project.users.set(users)
    #         return Response(serializer.data, status=HTTP_201_CREATED)

    #     return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

