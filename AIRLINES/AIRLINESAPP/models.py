from django.db import models
from django.db.models import F
import math

# Create your models here.

class AirplaneInfo(models.Model):
    airplane_id = models.PositiveIntegerField(primary_key=True)
    passenger_count = models.PositiveIntegerField()
    fuel_capacity_inlitres = models.GeneratedField(
            expression=F('airplane_id')*200,
            output_field=models.PositiveIntegerField(),
            db_persist=True,
    )
    #method to calculate fuel consumption in litres
    @property
    def fuel_consumption_inlitres(self): 
      return (math.log10(self.airplane_id * 0.80)+ (self.passenger_count*0.002))
      
    #method to calculate flying time in minutes
    @property
    def fly_time_inminutes(self): 
        return self.fuel_capacity_inlitres/self.fuel_consumption_inlitres

