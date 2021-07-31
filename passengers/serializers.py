from rest_framework import serializers
from passengers.models import Passengers

# Passenger Serializer
class PassengersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = '__all__'