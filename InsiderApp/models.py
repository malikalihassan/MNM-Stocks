from django.db import models

from StocksData.models import Stocks


# Create your models here.
class InsiderTransaction(models.Model):
    symbolKey = models.ForeignKey(Stocks, on_delete=models.CASCADE, related_name="symbolKey",null=True)
    name = models.CharField(max_length=50, null=True, default="")
    cost = models.FloatField(null=True)

