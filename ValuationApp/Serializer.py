from rest_framework import serializers


from ValuationApp.models import Valuation


class ValuationSearilizer(serializers.ModelSerializer):
    class Meta:
        model = Valuation
        fields = "__all__"

