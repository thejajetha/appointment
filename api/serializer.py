from rest_framework import serializers
from api.models import User
from api.models import Appointment


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=['id','username','email','password','phone']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:

        model=Appointment

        fields="__all__"

        read_only_fields=["id","customer",'created_at']

    def validate(self, data):
        
        if Appointment.objects.filter(date=data.get('date'),time_slot=data.get('time_slot')).exists():

            raise serializers.ValidationError("slot is already booked")
        
        return data

