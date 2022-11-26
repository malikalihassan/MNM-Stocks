from django.db import models


# Create your models here. 
# Symbol is intensionally varchar and primary key according to my understanding of the problem


class Stocks(models.Model):
    symbol = models.CharField(primary_key=True, max_length=50, unique=True)
    name = models.CharField(max_length=10, null=True, default="")
    price = models.IntegerField()
    change = models.FloatField()






