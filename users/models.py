from django.db import models
from catering.models import CateringProfile,FoodItem
from django.contrib.auth.models import User
# Create your models here.



# class FoodItem(models.Model):
#     food_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     image = models.ImageField(upload_to="foods", null=True, blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity_available = models.IntegerField(default=0)
#     quantity_booked = models.IntegerField(default=0)
#     booked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booked_items', null=True)
#     status = models.CharField(max_length=20, default='Pending')
#     def __str__(self):
#         return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile',null=True,blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.user.username
    
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.user.username} at {self.time}"    