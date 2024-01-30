from .models import AirplaneInfo
from rest_framework import serializers

# Airplane Serializer
class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:       
        model = AirplaneInfo
        # the fields that should be included in the serialized output
        fields = ['airplane_id','passenger_count','fuel_capacity_inlitres','fuel_consumption_inlitres','fly_time_inminutes']


