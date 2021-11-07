from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class People(models.Model):
    how_many = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    name=models.TextField(default = '')
    def __str__(self):
        return str(self.name)
    

class What_food(models.Model):
    point = models.IntegerField(default=0)
    who=models.ForeignKey(People, on_delete=models.CASCADE)
    date= models.IntegerField(default=20211106)
    month=models.IntegerField(default=0)



class Food(models.Model):
    def __init__(self,point):
        self.point = point


