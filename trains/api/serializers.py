from rest_framework import serializers
from .models import *

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ["id","name"]

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trains
        fields = ["id","name","count_seat"]

class TrainRouteSerializer(serializers.ModelSerializer):
    #from_city = CitySerializer(read_only=True)
    to_city = serializers.SerializerMethodField()
    # cities_count = serializers.SerializerMethodField()
    from_city = serializers.SerializerMethodField()
    remaining_seats = serializers.SerializerMethodField()
    is_purchased = serializers.SerializerMethodField()
    class Meta:
        model = TrainRoutes
        fields = ["id","from_city","from_time","to_city","to_time","cost","remaining_seats",'is_purchased']
        # fields = '__all__'

    def get_remaining_seats(self, obj):
        return obj.train.count_seat-len(Tickets.objects.filter(train_route=obj.id))
    
    def get_to_city(self, obj):
        return obj.to_city.name
    
    def get_from_city(self, obj):
        return obj.from_city.name
    
    def get_is_purchased(self, obj):
        tmp = len(Tickets.objects.filter(train_route=obj.id))
        return True if tmp > 0 else False
    
class TrainRouteDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainRoutes
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    # train_route = TrainRouteSerializer(read_only=True)
    from_city = serializers.SerializerMethodField()
    from_time = serializers.SerializerMethodField()
    to_city = serializers.SerializerMethodField()
    to_time = serializers.SerializerMethodField()
    cost = serializers.SerializerMethodField()
    class Meta:
        model = Tickets
        fields = ["id","from_city","from_time","to_city","to_time","cost"]

    def get_from_city(self, obj):
        return obj.train_route.from_city.name
    def get_from_time(self, obj):
        return obj.train_route.from_time
    def get_to_city(self, obj):
        return obj.train_route.to_city.name
    def get_to_time(self, obj):
        return obj.train_route.to_time
    def get_cost(self, obj):
        return obj.train_route.cost
    
class TicketDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'