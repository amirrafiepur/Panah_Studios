# Create your models here.

from django.db import models

class Human(models.Model):
    Id=models.AutoField(primary_key=True,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name +" " + self.last_name    


  