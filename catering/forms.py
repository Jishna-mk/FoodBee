from django.forms import ModelForm
from django import forms
from .models import FoodItem
from .models import CateringProfile
from django.forms import TextInput,Textarea,NumberInput,DateInput





class CateringProfileForm(ModelForm):
    class Meta:
        model = CateringProfile
        fields = ["Address","Catering_Name","Phone_Number","Designation"]

        widgets = {
            'Phone_Number': NumberInput(attrs={"class":"form-control","placeholder":"Enter Phone number"}),
            'Designation': TextInput(attrs={"class":"form-control","placeholder":"Enter  Your Designation"}),
            'Address': Textarea(attrs={"class":"form-control","placeholder":"Enter  Address"}),
            'Catering_Name': Textarea(attrs={"class":"form-control","placeholder":"Enter  Your Compant Name"}),
        }





class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'image', 'quantity_available']

    