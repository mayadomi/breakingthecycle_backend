from rest_framework import serializers
from .models import CustomUser
from django.apps import apps

class CustomUserDonationSerializer(serializers.ModelSerializer):
    donation = serializers.RelatedField(read_only=True)

    class Meta:
        model=apps.get_model('riders.Donation')
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):

    rider = serializers.ReadOnlyField(source='user.id')
    donations = CustomUserDonationSerializer(many=True, read_only=True, source='donor')
    
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
    

