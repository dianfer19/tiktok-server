#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Submit, Row, Column
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'cellphone', 'address', 'reference',
                  'razon_social', 'identificacion')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('cellphone', 'address', 'reference',
                  'razon_social', 'identificacion')
