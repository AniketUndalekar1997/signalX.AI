from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'city']
        labels = {'name': 'Name', 'city': 'City'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'city': forms.TextInput(attrs={'class': 'form-control'}),
                   }

