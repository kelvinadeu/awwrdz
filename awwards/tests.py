from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project,UserProfile

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='user-password')
        self.new_profile = UserProfile(id=1,user=self.new_user,bio='user-bio')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,UserProfile))
    
