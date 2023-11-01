from django.forms import ModelForm
from .models import Chamber

class ChamberForm(ModelForm):
    class Meta:
        Model = Chamber
        fields = '__all__'