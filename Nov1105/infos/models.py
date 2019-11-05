from django.db import models

# Create your models here.
class One(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

class Two(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    subdescription = models.TextField()
    def __str__(self):
        return self.title

class MainQuestion(models.Model):
    content = models.CharField(max_length=100)
    pick = models.IntegerField()
    