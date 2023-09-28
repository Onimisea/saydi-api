from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Donation

class CreateDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['first_name', 'last_name', 'email', 'frequency', 'amount', 'reference']

    def create(self, validated_data):
        """
        Create and return a new Donation instance, given the validated data.
        """
        return Donation.objects.create(**validated_data)

    
