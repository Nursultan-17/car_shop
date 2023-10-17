from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

def CarsView(request):
    cars = Car.objects.all()
    context = {
            'cars': cars,
        }
    return render(request=request, template_name='cars_template.html', context=context)



def CarDetailView(request, car_id):
    car = Car.objects.get(id=car_id)
    context = {
        'car': car
    }
    return render(request=request, template_name='car_detail_template.html', context=context)

def CarFView(request, car_brand):
    car = Car.objects.filter(brand=car_brand)
    context = {
        'car': car
    }
    return render(request=request, template_name='carf_template.html', context=context)


def CarCreateView(request):
    if request.method == 'GET':
        return render(request=request, template_name='car_create_template.html')
    elif request.method == 'POST':
        brand = request.POST.get('brand').capitalize()
        model = request.POST.get('model').capitalize()
        year = request.POST.get('year').capitalize()
        engine_capacity = request.POST.get('engine_capacity').capitalize()
        color = request.POST.get('color').capitalize()
        price = request.POST.get('price').capitalize()
        image = request.FILES.get('image')
        flower = Car(brand=brand,model=model,year=year,engine_capacity=engine_capacity, color=color,price=price, image=image)
        flower.save()
        return CarsView(request)