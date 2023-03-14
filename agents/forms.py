from django.forms import ModelForm
from leads.models import Agent, User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class AgentCreateForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email',)

class AgentUpdateForm(ModelForm):
    class Meta:
        model = Agent
        fields = ('image',)

