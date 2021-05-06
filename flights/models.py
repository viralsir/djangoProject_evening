from django.db import models
'''
    makemigrations --> create migrations
    migrate ==> apply change which define in the migrations file
'''
# Create your models here.
class flight(models.Model):
    source=models.CharField(max_length=20)
    destions=models.CharField(max_length=20)
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.source} - {self.destions}"