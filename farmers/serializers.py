from django import forms
from django.forms import widgets
from django.forms.extras.widgets import SelectDateWidget
from rest_framework import serializers
from farmers.models import Farmer, GENDER_CHOICES


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'gender', 'verified_date'
                    ,'date_of_birth','registration_date')

