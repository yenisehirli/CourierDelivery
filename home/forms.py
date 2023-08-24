from django import forms
from .models import User, CourierVehicle, NavigationRecord,Order,Client

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'email', 'phone']


class CourierVehicleForm(forms.ModelForm):
    class Meta:
        model = CourierVehicle
        fields = ['user', 'plate']

class NavigationRecordForm(forms.ModelForm):
    class Meta:
        model = NavigationRecord
        fields = ['vehicle', 'latitude', 'longitude', 'datetime']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['latitude', 'longitude', 'order_frequency', 'last_order_at', 'address_description']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'vehicle', 'created_at']



