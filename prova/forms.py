from django.forms import ModelForm
from .models import Dvd

class DvdForm(ModelForm):

    class Meta:
        model = Dvd
        fields = '__all__'