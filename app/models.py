from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    address=models.TextField()
    profilepic=models.ImageField()
    username=models.OneToOneField(User,on_delete=models.CASCADE)


