from django.forms import ModelForm
from django import forms
from .models import Lead, Category
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

class CreateCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

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





    