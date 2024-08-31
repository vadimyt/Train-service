from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.http import Http404
from datetime import datetime, timezone
# Create your views here.

def get_train_route_object(pk):
        try:
            return TrainRoutes.objects.get(pk=pk)
        except TrainRoutes.DoesNotExist:
            raise Http404
        
def get_city_object(pk):
        try:
            return Cities.objects.get(pk=pk)
        except Cities.DoesNotExist:
            raise Http404
        
def get_ticket_object(pk):
        try:
            return Tickets.objects.get(pk=pk)
        except Tickets.DoesNotExist:
            raise Http404

class TrainRoutesView(APIView):
    def get(self, request, format=None):
        trainroutes = TrainRoutes.objects.all()
        if (len(request.query_params)):
            train = self.request.query_params.get('train')
            if train:
                trainroutes = trainroutes.filter(train = train)

            from_city = self.request.query_params.get('from_city')
            if from_city:
                trainroutes = trainroutes.filter(from_city = from_city)

            from_time = self.request.query_params.get('from_time')
            if from_time:
                trainroutes = trainroutes.filter(from_time = from_time)

            to_city = self.request.query_params.get('to_city')
            if to_city:
                trainroutes = trainroutes.filter(to_city = to_city)

            to_time = self.request.query_params.get('to_time')
            if to_time:
                trainroutes = trainroutes.filter(from_time = from_time)

            cost = self.request.query_params.get('cost')
            if cost:
                trainroutes = trainroutes.filter(cost = cost)
        serializer = TrainRouteSerializer(trainroutes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TrainRouteView(APIView):
    def get(self, request, pk, format=None):
        trainroute = get_train_route_object(pk)          
        serializer = TrainRouteSerializer(trainroute)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CitiesView(APIView):
    def get(self, request, format=None):
        cities = Cities.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CityView(APIView):
    def get(self, request, pk, format=None):
        city = get_city_object(pk)   
        serializer = CitySerializer(city)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TicketsView(APIView):
    def get(self, request, format=None):
        tickets = Tickets.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = TicketDefaultSerializer(data=request.data)
        if serializer.is_valid():
            if (get_train_route_object(request.data['train_route']).from_time <= datetime.now(timezone.utc)):
                data = {"Error":"train_route time is up"}
                return Response(data, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TicketView(APIView):
    def get(self, request, pk, format=None):
        ticket = get_ticket_object(pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk, format=None):
        ticket = get_ticket_object(pk)
        if (ticket.train_route != None):
            if (ticket.train_route.from_time <= datetime.now(timezone.utc)):
                data = {"Error":"train_route time is up"}
                return Response(data, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)