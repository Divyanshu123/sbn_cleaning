from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Devotee(models.Model):
    info = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone_number = models.CharField(unique=True, max_length=12)
    score_of_week = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return self.info.username  

    



class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500,default='hare krishna')
    point = models.IntegerField(default=0)
    deadline = models.DateTimeField() 
    devotee = models.ForeignKey(Devotee,on_delete=models.CASCADE,related_name='services',null=True)
    taken = models.BooleanField(default = False)
    done = models.BooleanField(default=False)


    def __str__(self):
        return self.name  