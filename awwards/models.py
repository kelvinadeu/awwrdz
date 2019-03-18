from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length =30,null=True)
    profile_photo = models.ImageField(upload_to = 'pics/')
    bio = models.TextField(max_length=100,blank=True)
    user_id = models.OneToOneField(User,on_delete=models.CASCADE)
    
