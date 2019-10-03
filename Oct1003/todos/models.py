from django.db import models

# Create your models here.
class Todo(models.Model): # 추가
    title = models.CharField(max_length=50)
    due_date = models.DateField()