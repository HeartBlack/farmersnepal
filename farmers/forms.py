from django.forms import ModelForm
from .models import Place_order


class place_order(ModelForm):
         class Meta:
            model = Place_order
            fields = '__all__'
