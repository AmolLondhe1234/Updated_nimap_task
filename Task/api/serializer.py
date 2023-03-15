from rest_framework import serializers
from .models import Client,Project
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user    

class ProjectSerializer(serializers.ModelSerializer):
    client=serializers.ReadOnlyField(source='client.client_name')
    users = serializers.SlugRelatedField(
        many=True,
        queryset=User.objects.all(),
        slug_field='username'
     )
    class Meta:
        model=Project
        fields='__all__'
        
    # def get_users(self, obj):
    #     return obj.users.username

class ClientSerializer(serializers.ModelSerializer):
    # projects=ProjectSerializer(many=True,read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Client
        fields = ('id','client_name','created_at','created_by')
        
class  ClientDSerializer(serializers.ModelSerializer):
    projects=ProjectSerializer(many=True,read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')
    # updated_at=serializers.ReadOnlyField(source='updated_at')
    class Meta:
        model = Client
        fields = "__all__"        
    
    
    
    
