from django.db import models

from StocksData.models import Stocks


# Create your models here.


class Valuation(models.Model):
    symbol_key = models.OneToOneField(Stocks, on_delete=models.CASCADE, related_name='symbol_key')
    market_cap = models.DecimalField(max_digits=10, decimal_places=2)
    pe_ratio = models.FloatField()

