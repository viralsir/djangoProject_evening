from django.db import models
'''
    makemigrations --> create migrations
    migrate ==> apply change which define in the migrations file


    origin=Airport(code='bor',city='baroda')
    destions=Airport(code='mub',city='mumbai')
    
    fl=flight(origin=Airport(code='bor',city='baroda'),
                destions=Airport(code='mub',city='mumbai')
                )
    fl.origin.code => 'bor'
    
'''
# Create your models here.
class airport(models.Model):
    code=models.CharField(max_length=40)
    city=models.CharField(max_length=40)


    def __str__(self):
        return f"{self.city}({self.code})"

class flight(models.Model):
    origin=models.ForeignKey(airport,on_delete=models.CASCADE,related_name='departure')
    destions=models.ForeignKey(airport,on_delete=models.CASCADE,related_name='arrival')
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.origin} - {self.destions}"

class passenger(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=40)
    flights=models.ManyToManyField(flight,related_name='passenger')

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"
