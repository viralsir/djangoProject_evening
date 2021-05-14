from django.db import models

# Create your models here.
class course_master(models.Model):
    name=models.CharField(max_length=30)
    duration=models.IntegerField()
    description=models.TextField()
    fees=models.IntegerField()

    def __str__(self):
        return f"{self.name}-{self.fees}"
