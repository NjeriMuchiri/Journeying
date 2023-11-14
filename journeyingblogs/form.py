from django.forms import ModelForm
from .models import Chamber
from django.contrib.auth.models import User

#chamber form fields
class ChamberForm(ModelForm):
    class Meta:
        model = Chamber
        fields = '__all__'
        exclude = ['host', 'techiesspace']

#user profile forms
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']