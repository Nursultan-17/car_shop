from django.urls import path
from .views import *

urlpatterns = [
    path('cars', CarsView, name='cars_url'),
    path('car/<int:car_id>', CarDetailView, name='car_detail_url'),
    path('cars/<str:car_brand>', CarFView, name='carf_url'),
    path('cr_car', CarCreateView, name='car_create_url'),
    path('dl_car', CarDeleteView, name='car_delete_url'),

]