from django.forms import ModelForm
from django import forms
from .models import Lead
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Agent
User = get_user_model()

class CreateLeadForm(ModelForm):
    class Meta:
        model=Lead
        fields ='__all__'
        exclude = ('organization',)
        

class UserSignCustomForm(UserCreationForm):
    class Meta:
        model = User
        fields= ("username",)
        field_classes = {'username': UsernameField}

class AssignLeadForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self ,*args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organization=request.user.userprofile)
        super(AssignLeadForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents