from rest_framework import serializers
from InsiderApp.Serializer import InsiderSearilizer
from InsiderApp.models import InsiderTransaction
from StocksData.models import Stocks
from ValuationApp.Serializer import ValuationSearilizer

# You will fetch the 10 rows of insider transaction table, and the related data of
# valuation table using just one call on the stock table using symbol. Serializer


class StockDataSearilizer(serializers.ModelSerializer):
    symbol_key = ValuationSearilizer(many=False)
    symbolKey = InsiderSearilizer(many=True)

    class Meta:
        model = Stocks
        fields = "__all__"


# Write the post API to save data in the stock table and insider transactions table. Searilizer
class StockDataSearilizerForPOST(serializers.ModelSerializer):
    symbolKey = InsiderSearilizer()

    class Meta:
        model = Stocks
        fields = "__all__"

    def create(self, validated_data):
        symbolKey = validated_data.pop('symbolKey')
        stocks = Stocks.objects.create(**validated_data)
        InsiderTransaction.objects.create(symbolKey=stocks, **symbolKey)
        return stocks
