from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Customer

class RegistrationForm(UserCreationForm):
    
    email = forms.EmailField(max_length=50,widget=forms.EmailInput
                                (attrs={'placeholder' : 'Enter Email'}))

    class Meta:
        model = Customer
        
        fields = ('email' , 'username' , 'password1' , 'password2')
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({'placeholder' : 'Username'})
            self.fields['password1'].widget.attrs.update({'placeholder' : 'Enter Password'})
            self.fields['username'].widget.attrs.update({'placeholder' : 'Confirm Password'})

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            customer = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already exists' %customer )

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            customer = Customer.objects.get(username=username)
        except Customer.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already exists' %customer )

class CustomerAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password' , widget=forms.PasswordInput
                                (attrs={'placeholder' : 'Enter Password'}))

    class Meta:
        model = Customer
        fields = ('email'  , 'password')

    def clean(self):
        if self.is_valid:
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email , password = password):
                raise forms.ValidationError("Invalid Login")