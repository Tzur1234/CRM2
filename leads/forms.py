from django.forms import ModelForm
from django import forms
from .models import Lead, Category, FollowUp
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Agent
from django.core.exceptions import ValidationError
User = get_user_model()

class CreateLeadForm(ModelForm):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none(), required = False)    
    
    class Meta:
        model=Lead
        fields =(
            'first_name',
            'last_name',
            'email',
            'area_code',
            'phone',
            'image',
        )
        # exclude = ('organization', 'date_added', 'converted_date', 'agent', 'category',)

    def __init__(self ,*args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organization=request.user.userprofile)
        super(CreateLeadForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents

    # CUSROM VALIDATION
    # def clean_agent(self):
    #     agent = self.cleaned_data['agent']
    #     if agent.organization != self.request.user.organization:
    #         raise ValidationError(f"Agent organization mustt be {self.request.user.organization}")
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
        leads = Lead.objects.filter(organization=request.user.userprofile, category__name='Empty')
            
        super(AssignLeadToCategoryForm, self).__init__(*args, **kwargs)
        self.fields["leads"].queryset = leads
        self.fields["categories"].queryset = category

class CreateFollowUpForm(ModelForm):
    class Meta:
        model = FollowUp 
        exclude = ('date_added', 'lead',)




    