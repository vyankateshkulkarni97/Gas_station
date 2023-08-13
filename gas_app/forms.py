from django import forms
from .models import Service_Request , SupportRepresentative

class Service_Request_Form(forms.ModelForm):
    class Meta:
        model = Service_Request
        fields = ['service_type', 'description', 'files']

class Track_Status_Form(forms.Form):
    account_number = forms.CharField(max_length=20)

class SupportRepresentativeForm(forms.ModelForm):
    class Meta:
        model = SupportRepresentative
        fields = ['name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }