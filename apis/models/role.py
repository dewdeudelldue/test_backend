from django.db import models

class Role(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'roles'
        ordering = ['title']