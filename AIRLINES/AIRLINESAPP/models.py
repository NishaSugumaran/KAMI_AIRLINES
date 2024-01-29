from django.db import models
from django.db.models import F
import math

# Create your models here.

class Airplane(models.Model):
    airplane_id = models.IntegerField(default=1, blank=True)
    passenger = models.IntegerField(default=1, blank=True, null=True)
    fuel_capacity = models.GeneratedField(
            expression=F('airplane_id')*200,
            output_field=models.IntegerField(),
            db_persist=True,
    )
    @property
    def fuel_consumption_litres(self): 
      return (math.log10(self.airplane_id * 0.80)+ (self.passenger*0.002))
      

    @property
    def fly_time_minutes(self): 
        return self.fuel_capacity/self.fuel_consumption_litres


class AirplaneInfo(models.Model):
    airplane_id = models.PositiveIntegerField(primary_key=True)
    passenger_count = models.PositiveIntegerField()
    fuel_capacity_inlitres = models.GeneratedField(
            expression=F('airplane_id')*200,
            output_field=models.PositiveIntegerField(),
            db_persist=True,
    )
    @property
    def fuel_consumption_inlitres(self): 
      return (math.log10(self.airplane_id * 0.80)+ (self.passenger_count*0.002))
      

    @property
    def fly_time_inminutes(self): 
        return self.fuel_capacity_inlitres/self.fuel_consumption_inlitres

'''
    fuel_consumption = models.GeneratedField(
            expression=math.log(F('airplane_id'))*0.80 + F(passenger)*0.002,
            output_field=models.FloatField(),
            db_persist=True,
    )
    
    
    fuel_capacity = models.IntegerField(default=1, blank=True, null=True)
    fuel_consumption = models.GeneratedField(
            expression=F('airplane_id')*200,
            output_field=models.IntegerField(),
            db_persist=True,
    )
'''
