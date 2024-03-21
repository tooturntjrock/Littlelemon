from django.db import models


# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    numer_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def get_item(self):
        return f'{self.name}'

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

