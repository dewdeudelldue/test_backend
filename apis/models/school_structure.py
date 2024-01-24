from django.db import models

class SchoolLevel(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        db_table = 'school_levels'

class Grade(models.Model):
    title = models.CharField(max_length=100)
    school_level = models.ForeignKey(SchoolLevel, related_name='grades', on_delete=models.CASCADE)
    class Meta:
        db_table = 'grades'

class Room(models.Model):
    title = models.CharField(max_length=100)
    grade = models.ForeignKey(Grade, related_name='rooms', on_delete=models.CASCADE)
    class Meta:
        db_table = 'rooms'