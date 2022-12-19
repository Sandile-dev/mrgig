import django_filters
from .models import *
from django import forms


class ParcelFilter(django_filters.FilterSet):
    class Meta:
        model = Parcel
        fields = '__all__'
        exclude = ['customer','partner', 'origination', 'destination', 'status', 'date_created']
        widgets = {
            'refNumber':forms.TextInput(attrs={'class':'form-control" type="text" placeholder="Default input" aria-label="default input'}),
         }


class RouterFilter(django_filters.FilterSet):
    class Meta:
        model = DriverRoute
        fields = '__all__'
        exclude = ['city','town','rankName','date_created']
        widgets = {
            'province':forms.Select(attrs={'class':'form-control'})
        } 


class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['sender_surname','receiver_name','receiver_surname','receiver_phone','notification','date_created']
        widgets = {
            'sender_phone':forms.TextInput(attrs={'class':'form-control'}),
            'sender_name':forms.TextInput(attrs={'class':'form-control'})
        }