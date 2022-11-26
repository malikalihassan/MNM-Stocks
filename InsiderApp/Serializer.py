from rest_framework import serializers

from InsiderApp.models import InsiderTransaction


class LastTenRecords(serializers.ListSerializer):
    def to_representation(self, data):
        accurate_data = len(data.all())
        if accurate_data >= 10:
            data = data.all()[accurate_data - 10:accurate_data]
        else:
            data = data.all()

        return super(LastTenRecords, self).to_representation(data)


class InsiderSearilizer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = LastTenRecords
        model = InsiderTransaction
        fields = "__all__"
