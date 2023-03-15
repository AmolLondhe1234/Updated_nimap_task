from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import User




class Client(models.Model):
    client_name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE )
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.client_name
    
    
    
class Project(models.Model):
    project_name=models.CharField(max_length=50)
    users=models.ManyToManyField(User)
    client=models.ForeignKey(Client, related_name='projects',on_delete=models.CASCADE)    