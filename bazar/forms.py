from django.forms import ModelForm
from .models import *


class TeniskyModelForm(ModelForm):
    class Meta:
        model = Tenisky
        fields = ['nazev','popis','velikost','cena','cena1']
