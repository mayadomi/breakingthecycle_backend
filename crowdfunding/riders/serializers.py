from rest_framework import serializers
from django.apps import apps


class DonationSerializer(serializers.ModelSerializer):

    donor = serializers.ReadOnlyField(source='donor.id')

    class Meta:
        model = apps.get_model('riders.Donation')
        fields = '__all__'


class RiderUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = apps.get_model('riders.RiderUpdates')
        fields = "__all__"


class RiderSerializer(serializers.ModelSerializer):  

    rider_id = serializers.ReadOnlyField(source='id')
    rider_user_id = serializers.ReadOnlyField(source='rider.id')
    rider_user_name = serializers.ReadOnlyField(source='rider.username')

    class Meta:
        model = apps.get_model('riders.Rider')      
        fields = ('rider_id', 'rider_user_id', 'rider_user_name', 'team', 'bio', 'avatar_image', 'background_image', 'is_active', 'date_created', 'rate', 'kms_ceiling', 'kms_ridden', 'amount_donated', 'kms_to_ride')


class RiderDetailSerializer(RiderSerializer):
    donations = DonationSerializer(many=True, read_only=True)
    updates = RiderUpdateSerializer(many=True, read_only=True)

    rider_id = serializers.ReadOnlyField(source='id')
    rider_user_id = serializers.ReadOnlyField(source='rider.id')
    rider_user_name = serializers.ReadOnlyField(source='rider.username')

    def update(self, instance, validated_data):
        instance.rider = validated_data.get('rider', instance.rider)
        instance.team = validated_data.get('team', instance.team)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.avatar_image = validated_data.get('avatar_image', instance.avatar_image)
        instance.background_image = validated_data.get('background_image', instance.background_image)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.kms_ceiling = validated_data.get('kms_ceiling', instance.kms_ceiling)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.save()
        return instance
    
    class Meta:
        model = apps.get_model('riders.Rider')
        fields = fields = ('rider_id', 'rider_user_id', 'rider_user_name', 'team', 'bio', 'avatar_image', 'background_image', 'is_active', 'date_created', 'rate', 'kms_ceiling', 'kms_ridden', 'amount_donated', 'kms_to_ride', 'donations', 'updates')
    
