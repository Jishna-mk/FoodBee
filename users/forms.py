from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
import re
from django.forms import TextInput,ModelForm,DateInput
from .models import UserProfile,Feedback

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email','phone_number', 'address', ]


class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            'username': TextInput(attrs={"class": "form-control"}),
            'email': TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content']






# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['quantity', 'address','phone_number']
        