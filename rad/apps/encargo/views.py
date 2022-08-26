from django.shortcuts import render
from django.views.generic.edit import CreateView

from apps.encargo.models import Encargo
from apps.encargo.forms import RegistroEncargoFrom
# Create your views here.

class addEncargo(CreateView):
    model = Encargo
    form_class = RegistroEncargoFrom
    template_name = 'encargo/addEncargo.html'