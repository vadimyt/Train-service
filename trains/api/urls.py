from django.urls import path
from . import views

urlpatterns = [
    path("train_routes", views.TrainRoutesView.as_view(), name="trainroutes"),
    path("train_routes/<int:pk>", views.TrainRouteView.as_view(), name="trainroute"),
    path("cities", views.CitiesView.as_view(), name="cities"),
    path("cities/<int:pk>", views.CityView.as_view(), name="city"),
    path("tickets", views.TicketsView.as_view(), name="tickets"),
    path("tickets/<int:pk>", views.TicketView.as_view(), name="ticket"),
]