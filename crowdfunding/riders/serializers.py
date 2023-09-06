from rest_framework import serializers
from django.apps import apps


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('riders.Donation')
        fields = '__all__'


class RiderSerializer(serializers.ModelSerializer):
    rider_owner = serializers.ReadOnlyField(source='rider_owner.id')

    class Meta:
        model = apps.get_model('riders.Rider')
        fields = '__all__'


class RiderDetailSerializer(RiderSerializer):
    donations = DonationSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.team = validated_data.get('team', instance.team)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.avatar_image = validated_data.get('avatar_image', instance.avatar_image)
        instance.background_image = validated_data.get('background_image', instance.background_image)
        instance.is_active = validated_data.get('is_active', instance.background_image)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.kms_goal = validated_data.get('kms_goal', instance.kms_goal)
        instance.kms_ridden = validated_data.get('kms_goal', instance.kms_ridden)
        instance.rider_owner = validated_data.get('rider_owner', instance.rider_owner)
        instance.save()
        return instance