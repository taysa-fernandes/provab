from django.forms import ModelForm
from django import forms
from .models import Curso
class CursoForm(ModelForm):

    class Meta:
        model = Curso
        fields = '__all__'