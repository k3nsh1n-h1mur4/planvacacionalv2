from django import forms
from django.contrib.auth.forms import BaseUserCreationForm



class CustomUserForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario: ',
                  widget=forms.TextInput(),
                  required=False
                )
    

