from django.db import models

# Create your models here.
class Big(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    description = models.TextField()

class Small(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    description = models.TextField()

class Hashtag(models.Model):
    content = models.CharField(max_length=50)
    bigs = models.ManyToManyField(Big, related_name="big_hashtags")
    smalls = models.ManyToManyField(Small, related_name="small_hashtags")