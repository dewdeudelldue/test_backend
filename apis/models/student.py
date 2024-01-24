from django.db import models
from .teacher import Teacher
from .school import School
from .classes import Classes

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    class_assigned = models.ForeignKey(Classes, on_delete=models.CASCADE)
    head_of_room = models.BooleanField(default=False)
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)


    class Meta:
        db_table = 'students'