from django.db import models

# Create your models here.


class Task(models.Model):
    tname = models.CharField(max_length=100)
    tdesc = models.TextField()
    
    

    
    # completed = models.BooleanField(default=False)
    
    
    # roll = models.IntegerField()
    # price = models.DecimalField()