from django.urls import path
from . import views

urlpatterns = [
    path("train_routes", views.TrainRoutesGetPostPut.as_view(), name="trainroutes"),
    path("train_routes/<int:pk>", views.TrainRouteGetDelete.as_view(), name="trainroute")
]