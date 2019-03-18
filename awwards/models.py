from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length =30,null=True)
    profile_photo = models.ImageField(upload_to = 'pics/')
    bio = models.TextField(max_length=100,blank=True)
    user_id = models.OneToOneField(User,on_delete=models.CASCADE)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def save_user(self):
        self.save()

    @classmethod
    def search_user(cls,username):
        searched_user = User.objects.get(username = username)
        return searched_user

    def __str__(self):
        return self.user.username
