from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
# Create your models here.

class customUser(AbstractUser):
    age = models.PositiveBigIntegerField(null=True,blank=True)
    

