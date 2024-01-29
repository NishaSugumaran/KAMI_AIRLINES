from .models import AirplaneInfo
#from django.contrib.auth.models import User, Group
from rest_framework import serializers
'''
class AirplaneListSerializer(serializers.ListSerializer):
    def do_stuff(data):
        return data
    def create(self, validated_data):
        airplane = [airplane(**item) for item in validated_data]
        return Airplane.objects.bulk_create(airplane)
'''
# Airplane Serializer
class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:       
        model = AirplaneInfo
        #list_serializer_class = AirplaneListSerializer
        # the fields that should be included in the serialized output
        fields = ['airplane_id','passenger_count','fuel_capacity_inlitres','fuel_consumption_inlitres','fly_time_inminutes']
        #fields = ['airplane_id','passenger','fuel_capacity']

