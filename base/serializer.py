from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        # You can enter a list of parameters here if you what to send specific data
        # fields = ["names","description"]
        fields = '__all__' # to return back everything