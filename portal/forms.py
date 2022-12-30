from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('sender_name','sender_surname','sender_phone','receiver_name','receiver_surname','receiver_phone','notification')
        widgets = {
            'sender_name':forms.TextInput(attrs={'class':'form-control'}),
            'sender_surname':forms.TextInput(attrs={'class':'form-control'}),
            'sender_phone':forms.TextInput(attrs={'class':'form-control'}),
            'receiver_name':forms.TextInput(attrs={'class':'form-control'}),
            'receiver_surname':forms.TextInput(attrs={'class':'form-control'}),
            'receiver_phone':forms.TextInput(attrs={'class':'form-control'}),
            'notification':forms.Select(attrs={'class':'form-control'})
        }


class ParcelForm(ModelForm):
    class Meta:
        model = Parcel
        fields = ('refNumber','customer','origination','destination','status')
        widgets = {
            'refNumber':forms.TextInput(attrs={'class':'form-control'}),
            'customer':forms.Select(attrs={'class':'form-control'}),
            'origination':forms.TextInput(attrs={'class':'form-control'}),
            'destination':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
        }


class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = ('parcel','name','phoneNumber','taxiRegNumber','driver_route')
        widgets = {
            'parcel':forms.Select(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phoneNumber':forms.TextInput(attrs={'class':'form-control'}),
            'taxiRegNumber':forms.TextInput(attrs={'class':'form-control'}),
            'driver_route':forms.Select(attrs={'class':'form-control'}),
        }


class RouterForm(ModelForm):
    class Meta:
        model = DriverRoute
        fields = ('province','city','town','rankName')
        widgets = {
            'province':forms.Select(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'town':forms.TextInput(attrs={'class':'form-control'}),
            'rankName':forms.TextInput(attrs={'class':'form-control'}),
        }
        


class SignupUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ApplicationForm(forms.Form):
    fname = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'text',
        'placeholder': 'Enter your name'
    }))
    lname = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'text',
        'placeholder': 'Enter surname'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'text',
        'placeholder': 'Enter your cellphone'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'email',
        'placeholder': 'Enter e-mail address'
    }))
    raddress = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control form-control-lg',
        'type':'text',
        'placeholder': 'Enter residential address'
    }))
    job = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'text',
        'placeholder': 'Enter job title: Parcel Master / Runner'
    }))
    province = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'text',
        'placeholder': 'Enter your province'
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'text',
        'placeholder': 'Enter your city'
    }))
    motivation = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control form-control-lg',
        'type':'text',
        'placeholder': 'Provide your short business background'
    }))
        
