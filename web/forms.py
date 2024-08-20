from django import forms
from django.contrib.auth.models  import User
from .models import ContactForm, Profile

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']

#* REGISTER FORMS
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'message']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']