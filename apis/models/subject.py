from django.db import models

class Subject(models.Model):
    title = models.CharField(max_length=255)
    credit = models.IntegerField()

    class Meta:
        db_table = 'subjects'