from django.forms import ModelForm
from .models import Lead
   

class CreateLeadForm(ModelForm):
    class Meta:
        model=Lead
        fields ='__all__'
        