from django.db import models
from profiles.models import Profile

# Create your models here.

class PlasticData(models.Model):
    manager = models.ForeignKey(Profile,on_delete=models.CASCADE)
    shopname = models.CharField(max_length=200)
    product  = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    plastic_type = models.CharField(max_length=200) # 4 choices
    #  manager = profile.user
    status = models.CharField(max_length=200) # 4 choices
    
    