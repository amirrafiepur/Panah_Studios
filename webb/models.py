# Create your models here.

from django.db import models
import datetime

class Human(models.Model):
    Id=models.AutoField(primary_key=True,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name +" " + self.last_name    


class Expense(models.Model):
    expenseId=models.AutoField(primary_key=True,unique=True)
    date=models.DateTimeField(datetime.datetime.now())
    amount=models.BigIntegerField()
    user=models.ForeignKey(Human,on_delete=models.PROTECT)