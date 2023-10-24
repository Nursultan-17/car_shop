from django.urls import path
from .views import *

urlpatterns = [
    path('cars', carsView, name='cars_url'),
    path('car/<int:car_id>', carDetailView, name='car_detail_url'),
    path('cars/<str:car_brand>', carFView, name='carf_url'),

    path('cr_car', carCreateView, name='car_create_url'),
    path('dl_car', carDeleteView, name='car_delete_url'),
    path('up_car/<int:car_id>', carUpdateView, name='car_update_url'),

    path('log_in/', logInView, name='log_in_url'),
    path('log_out/', logOutView, name='log_out_url'),
    path('registration/', registrationView, name='registration_url'),

    path('sign_up/',sign_upView,name='sign_up_url')

]