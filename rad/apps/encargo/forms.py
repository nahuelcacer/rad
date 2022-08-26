from .models import Encargo
from django.db import transaction
from django.forms import ModelForm

class RegistroEncargoFrom(ModelForm):
    class Meta:
        model = Encargo
        fields = ['cliente','vehiculo', 'presupuesto' ]