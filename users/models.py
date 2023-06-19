from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class UserDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)   
    phone = models.CharField(max_length=12,blank= False,null=False)
    age = models.IntegerField()
    weight = models.FloatField()

class Items(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calorie = models.FloatField()
    date = models.DateField(_("Date"), default=datetime.date.today)
    time = datetime.now()

class UserManager(models.Model):
    user_manager = models.OneToOneField(User,on_delete=models.CASCADE)   
    phone = models.CharField(max_length=12,blank= False,null=False)
    age = models.IntegerField()
    weight = models.FloatField()

class Admin(models.Model):
    admin = models.OneToOneField(User,on_delete=models.CASCADE)   
    phone = models.CharField(max_length=12,blank= False,null=False)
    age = models.IntegerField()
    weight = models.FloatField()