from django.forms import ModelForm
from .models import Lead
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()

class CreateLeadForm(ModelForm):
    class Meta:
        model=Lead
        fields ='__all__'
        

class UserSignCustomForm(UserCreationForm):
    class Meta:
        model = User
        fields= ("username",)
        field_classes = {'username': UsernameField}