from django.forms import ModelForm
from .models import Chamber

class ChamberForm(ModelForm):
    class Meta:
        model = Chamber
        fields = '__all__'
        exclude = ['host', 'techiesspace']