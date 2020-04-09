from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    roll_no = forms.CharField(max_length=100, help_text='Roll No.')
    phone_no = forms.CharField(max_length=100, help_text='Phone No.')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'roll_no', 'phone_no', 'password1', 'password2',)
