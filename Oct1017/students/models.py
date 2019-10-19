from django.db import models

# Create your models here.
class Coffee(models.Model):
    menu = models.CharField(max_length=100)
    people = models.IntegerField()
    table = models.IntegerField()

class Flavor(models.Model):
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    star = models.IntegerField()
    memo = models.CharField(max_length=100)   