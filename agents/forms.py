from django.forms import ModelForm
from leads.models import Agent

class AgentCreateForm(ModelForm):
    class Meta:
        model = Agent
        fields = ['user']

