from django.db import models
from .student import Student
from .subject import Subject

class Score(models.Model):
    student = models.ForeignKey(Student, related_name='scores', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='scores', on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        db_table = 'scores'