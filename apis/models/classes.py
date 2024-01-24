from django.db import models
from .school import School

class Classes(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    class Meta:
        db_table = 'classes'