from django import forms
from .models import RegisterModel

class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterModel
        fields = [
            "name",
            "email",
            "Password",
        ]