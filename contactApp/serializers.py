from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import ContactBook

class ContactSerializers(ModelSerializer):
    class Meta:
        model = ContactBook
        fields='__all__'
       


