from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm

def carsView(request):
    cars = Car.objects.all()
    context = {
            'cars': cars,
        }
    return render(request=request, template_name='cars_template.html', context=context)



def carDetailView(request, car_id):
    car = Car.objects.get(id=car_id)
    context = {
        'car': car
    }
    return render(request=request, template_name='car_detail_template.html', context=context)

def carFView(request, car_brand):
    car = Car.objects.filter(brand=car_brand)
    context = {
        'car': car
    }
    return render(request=request, template_name='carf_template.html', context=context)


def carCreateView(request):
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
        return redirect('cars_url')

def carDeleteView(request):
    if request.method == 'GET':

        return render(request=request, template_name='car_delete_template.html')
    elif request.method == 'POST':
        car_delete = request.POST.get('model').capitalize()
        instance = Car.objects.get(model=car_delete)
        instance.delete()
        return redirect('cars_url')



def carUpdateView(request, car_id):
    if request.method == 'GET':
        car = Car.objects.get(id=car_id)
        context = {
            'cars': car,
        }
        return render(request=request, template_name='car_update_template.html', context=context)
    elif request.method == 'POST':
        car = Car.objects.get(id=car_id)
        car.brand = request.POST.get('brand').capitalize()
        car.model = request.POST.get('model').capitalize()
        car.year = request.POST.get('year').capitalize()
        car.engine_capacity = request.POST.get('engine_capacity').capitalize()
        car.color = request.POST.get('color').capitalize()
        car.price = request.POST.get('price').capitalize()
        if 'image' in request.FILES:
            car.image = request.FILES.get('image')
        car.save()
        return redirect('cars_url')



def logInView(request):
    if request.user.is_authenticated:
        return redirect('about_us_url')
    if request.method == 'GET':
        return render(request=request, template_name='log_in.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        # authenticate - Делает запрос в БД, ищет пользователя с таким username, хэширует пароль и сравнивает.
        # Если данные верны, то мы получим объект user. Если нет, то None.
        if user is not None:
            login(request, user)
            # login - регистрирует юзера в системе как юзера который уже вошел и выдает ему sessionid.
            # sessionid и csrftoken Джанго хранит в БД в своей таблице. После выхода из системы, он их удаляет.
            return redirect('cars_url')
        return redirect('log_in_url')


def logOutView(request):
    if request.user.is_authenticated:
        logout(request)
        # logout - находит связанные с юзером sessionid и csrftoken и удаляет их из БД.
    return redirect('log_in_url')


def registrationView(request):
    if request.method == 'GET':
        form = RegistrationForm()
        context = {
            'reg_form': form
        }
        return render(request=request, template_name='registration.html', context=context)
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in_url')
        return redirect('registration_url')