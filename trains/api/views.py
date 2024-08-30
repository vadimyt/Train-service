from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import TrainRoute
from .serializers import TrainRouteSerializer
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.

class TrainRoutesGetPostPut(APIView):
    def get_object(self, pk):
        try:
            return TrainRoute.objects.get(pk=pk)
        except TrainRoute.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        trainroute = TrainRoute.objects.all()
        if (len(request.query_params)):
            from_city = self.request.query_params.get('from_city')
            if from_city:
                trainroute = trainroute.filter(from_city = from_city)

            from_time = self.request.query_params.get('from_time')
            if from_time:
                trainroute = trainroute.filter(from_time = from_time)

            to_city = self.request.query_params.get('to_city')
            if to_city:
                trainroute = trainroute.filter(to_city = to_city)

            to_time = self.request.query_params.get('to_time')
            if to_time:
                trainroute = trainroute.filter(from_time = from_time)

            cost = self.request.query_params.get('cost')
            if cost:
                trainroute = trainroute.filter(cost = cost)
        serializer = TrainRouteSerializer(trainroute, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TrainRouteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, format=None):
        trainroute = self.get_object(request.data['id'])
        serializer = TrainRouteSerializer(trainroute, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrainRouteGetDelete(APIView):
    def get_object(self, pk):
        try:
            return TrainRoute.objects.get(pk=pk)
        except TrainRoute.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        trainroute = self.get_object(pk)          
        serializer = TrainRouteSerializer(trainroute)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk, format=None):
        trainroute = self.get_object(pk)
        trainroute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)