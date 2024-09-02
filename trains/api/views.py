from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.http import Http404
from datetime import datetime, timezone
from drf_yasg.utils import swagger_auto_schema
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
    @swagger_auto_schema(operation_description="Get train routes", query_serializer=TrainRouteDefaultSerializer, responses={200: TrainRouteSerializer(many=True)})
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
                from_time = (datetime.fromisoformat(from_time))
                trainroutes = trainroutes.filter(from_time__day = from_time.day, from_time__month = from_time.month, from_time__year = from_time.year)

            to_city = self.request.query_params.get('to_city')
            if to_city:
                trainroutes = trainroutes.filter(to_city = to_city)

            to_time = self.request.query_params.get('to_time')
            if to_time:                
                to_time = (datetime.fromisoformat(to_time))
                trainroutes = trainroutes.filter(to_time__day = to_time.day, to_time__month = to_time.month, to_time__year = to_time.year)

            cost = self.request.query_params.get('cost')
            if cost:
                trainroutes = trainroutes.filter(cost = cost)
        serializer = TrainRouteSerializer(trainroutes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TrainRouteView(APIView):
    @swagger_auto_schema(operation_description="Get single train route", responses={200: TrainRouteSerializer()})
    def get(self, request, pk, format=None):
        trainroute = get_train_route_object(pk)          
        serializer = TrainRouteSerializer(trainroute)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CitiesView(APIView):
    @swagger_auto_schema(operation_description="Get cities", responses={200: CitySerializer(many=True)})
    def get(self, request, format=None):
        cities = Cities.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CityView(APIView):
    @swagger_auto_schema(operation_description="Get city", responses={200: CitySerializer()})
    def get(self, request, pk, format=None):
        city = get_city_object(pk)   
        serializer = CitySerializer(city)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TicketsView(APIView):
    @swagger_auto_schema(operation_description="Get tickets", responses={200: TicketSerializer(many=True), 401: "status.HTTP_401_UNAUTHORIZED"})
    def get(self, request, format=None):
        if request.user.is_authenticated:
            tickets = Tickets.objects.all().filter(user=request.user)
            serializer = TicketSerializer(tickets, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    @swagger_auto_schema(request_body=TicketDefaultSerializer)
    def post(self, request, format=None):
        if request.user.is_authenticated:
            serializer = TicketDefaultSerializer(data=request.data)
            if serializer.is_valid():
                if (get_train_route_object(request.data['train_route']).from_time <= datetime.now(timezone.utc)):
                    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
                elif (request.user.id != request.data['user']):
                    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
                else:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
class TicketView(APIView):
    @swagger_auto_schema(operation_description="Get ticket", responses={200: TicketSerializer(), 401: "status.HTTP_401_UNAUTHORIZED", 405: "status.HTTP_405_METHOD_NOT_ALLOWED"})
    def get(self, request, pk, format=None):
        if request.user.is_authenticated:
            ticket = get_ticket_object(pk)
            if (ticket.user == request.user):
                serializer = TicketSerializer(ticket)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    @swagger_auto_schema(operation_description="Delete ticket", responses={204: "status.HTTP_204_NO_CONTENT", 401: "status.HTTP_401_UNAUTHORIZED", 405: "status.HTTP_405_METHOD_NOT_ALLOWED"})
    def delete(self, request, pk, format=None):
        if request.user.is_authenticated:
            ticket = get_ticket_object(pk)
            if (ticket.train_route != None):
                if (ticket.train_route.from_time <= datetime.now(timezone.utc)):
                    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
            else:
                if (ticket.user != request.user):
                    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
            ticket.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)