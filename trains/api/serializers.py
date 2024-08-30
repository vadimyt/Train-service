from rest_framework import serializers
from .models import TrainRoute

class TrainRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainRoute
        fields = ["id","from_city","from_time","to_city","to_time","cost"]