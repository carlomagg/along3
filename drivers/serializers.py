from rest_framework import serializers
from drivers.models import Drivers

# Passenger Serializer
class DriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = '__all__'