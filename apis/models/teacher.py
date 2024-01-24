from django.db import models
from .classes import Classes

class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    class_assigned = models.ForeignKey(Classes, on_delete=models.CASCADE)

    class Meta:
        db_table = 'teachers'
        