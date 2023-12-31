from datetime import timezone
from django.db import models
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
from django.db import models
from django.utils import timezone
from datetime import timedelta
# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=255,default="Yes")
    


class AddStation(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    station_name = models.CharField(max_length=255)
    location_city = models.CharField(max_length=255)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    owner_name = models.CharField(max_length=255)
    slots_number = models.IntegerField()
    timing = models.CharField(max_length=255)
    user_email = models.EmailField(null=True, default=None)  # Nullable field with default value
    password = models.CharField(max_length=128, null=True, default=None)  # Nullable field with default value
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, default='station')



class EVUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=255,default="Yes")
class UserBill(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    username = models.CharField(max_length=100)
    userid = models.IntegerField()
    stationid = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True) 
    rating = models.IntegerField(max_length=10, null=True, default=None)  
class Rating(models.Model):
    user_id = models.IntegerField()
    station_id = models.IntegerField()
    bill_id = models.IntegerField()
    rating_number = models.IntegerField()     
class Booking(models.Model):
    id = models.AutoField(primary_key=True, unique=True)

    ev_user = models.ForeignKey(EVUser, on_delete=models.CASCADE)
    add_station = models.ForeignKey(AddStation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking ID: {self.id}"


@receiver(post_save, sender=Booking)
def delete_after_duration(sender, instance, **kwargs):
    if timezone.now() - instance.created_at > timedelta(minutes=5):
        instance.delete()

class UserPayment(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=255)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ev_user = models.ForeignKey(EVUser, on_delete=models.CASCADE)