from django.forms import ModelForm
from leads.models import Agent
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class AgentCreateForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'email',
        )

