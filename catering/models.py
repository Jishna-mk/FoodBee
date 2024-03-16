from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class CateringProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    Phone_Number = models.IntegerField()
    Address = models.CharField(max_length=250)
    Catering_Name = models.CharField(max_length=250)
    Designation = models.CharField(max_length=250)

    def __str__(self):
        return self.Catering_Name

class FoodItem(models.Model):
    food_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="foods", null=True, blank=True)
    catering_name = models.CharField(max_length=200)
    quantity_available = models.IntegerField(default=0)
    quantity_booked = models.IntegerField(default=0)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booked_items', null=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.name
    
    def book_item(self, quantity, user):
        if quantity <= self.quantity_available:
            self.quantity_available -= quantity
            self.quantity_booked += quantity
            self.booked_by = user  
          
            self.save()
           
        return 0, False
    
