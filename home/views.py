from django.shortcuts import render, redirect
from .models import User, CourierVehicle
from .forms import UserForm, CourierVehicleForm, NavigationRecordForm,ClientForm,OrderForm



def create_record(request):
    users = User.objects.all()
    vehicles = CourierVehicle.objects.all()


    if request.method == 'POST':
        user_form = UserForm(request.POST)
        vehicle_form = CourierVehicleForm(request.POST)
        record_form = NavigationRecordForm(request.POST)

        if user_form.is_valid() and vehicle_form.is_valid() and record_form.is_valid():
            user = user_form.save()
            vehicle = vehicle_form.save(commit=False)
            vehicle.user = user
            vehicle.save()

            record = record_form.save(commit=False)
            record.user_id = user.id
            record.vehicle_id = vehicle.id
            record.save()

            return redirect('create_record')

    else:
        user_form = UserForm()
        vehicle_form = CourierVehicleForm()
        record_form = NavigationRecordForm()

    context = {
        'users': users,
        'vehicles': vehicles,
        'user_form': user_form,
        'vehicle_form': vehicle_form,
        'record_form': record_form,
    }

    return render(request, 'create_record.html', context)


def create_client(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client_form.save()
            return redirect('create_client')
    else:
        client_form = ClientForm()

    context = {'client_form': client_form}
    return render(request, 'create_client.html', context)


def create_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return redirect('create_order')
    else:
        order_form = OrderForm()

    context = {'order_form': order_form}
    return render(request, 'create_order.html', context)
