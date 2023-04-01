from django.db import models
from django.contrib.auth.models import User

# User Profile
class CustomUser(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    userType = models.CharField(max_length=50)
