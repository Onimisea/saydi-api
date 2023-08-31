from rest_framework import serializers
from .models import VolunteeringApplication

class VolunteeringApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteeringApplication
        fields = ['firstname', 'lastname', 'gender', 'email', 'state', 'lga', 'areas_of_interest', 'professional_background',  'how_you_find_us', ]
