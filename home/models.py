from django.db import models



class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CourierVehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plate = models.CharField(max_length=10)

    def __str__(self):
        return self.plate


class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(CourierVehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.vehicle.plate} - {self.datetime}"

class Client(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    order_frequency = models.IntegerField()
    last_order_at = models.DateTimeField()
    address_description = models.TextField()

    def __str__(self):
        return f"Müşteri {self.id}"

class Order(models.Model):
    name = models.CharField(max_length=255)
    vehicle = models.ForeignKey(CourierVehicle, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name


