from django.forms import ModelForm
from django import forms
from .models import Lead, Category
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Agent
from django.core.exceptions import ValidationError
User = get_user_model()

class CreateLeadForm(ModelForm):
    class Meta:
        model=Lead
        fields ='__all__'
        exclude = ('organization',)

    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if data != "Joe":
    #         raise ValidationError("First name must be equal to Joe")
    #     return data

    # def clean(self):
    #     first_name = self.cleaned_data['first_name']
    #     last_name = self.cleaned_data['last_name']

    #     if first_name + last_name != "Joe Soap":
    #         raise ValidationError("Your name is not equal to Joe Soap")


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

class CreateCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'html_class',)

class AssignLeadToCategoryForm(forms.Form):
    leads = forms.ModelChoiceField(Lead.objects.none())
    categories = forms.ModelChoiceField(Category.objects.none())
    

    def __init__(self ,*args, **kwargs):
        request = kwargs.pop("request")
        category = kwargs.pop("category")
        

        # Fetch only unassign leads
        leads = Lead.objects.filter(organization=request.user.userprofile, category__isnull=True)
            
        super(AssignLeadToCategoryForm, self).__init__(*args, **kwargs)
        self.fields["leads"].queryset = leads
        self.fields["categories"].queryset = category





    