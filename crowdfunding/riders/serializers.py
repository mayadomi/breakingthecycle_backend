from rest_framework import serializers
from django.apps import apps
from django.db.models import Sum

class DonationSerializer(serializers.ModelSerializer):
    donor = serializers.ReadOnlyField(source='donor.id')
    class Meta:
        model = apps.get_model('riders.Donation')
        fields = '__all__'

class RiderUpdateSerializer(serializers.ModelSerializer):

    rider = serializers.ReadOnlyField(source='rider_updates.id')

    class Meta:
        model = apps.get_model('riders.RiderUpdates')
        fields = "__all__"



class RiderSerializer(serializers.ModelSerializer):

    rider_owner = serializers.ReadOnlyField(source='rider_owner.id')

    class Meta:
        model = apps.get_model('riders.Rider')
        fields = '__all__'

class RiderDeSerializer(serializers.ModelSerializer):
        
    #kms_ridden = RiderUpdateSerializer(read_only=True, source='rider_updates', many=True)

    kms_ridden = serializers.ReadOnlyField(source='calc_kms_ridden')
    
    # @classmethod
    # def calc_kms_ridden(self, instance):
    #         print("its calcing")
    #         rider_updates = apps.get_model('riders.RiderUpdates')
    #         calcs = rider_updates.objects.get(rider=instance.rider_owner)
    #         total_kms = calcs.aggregate(s=Sum('kms_ridden'))["s"]
    #         return(total_kms)
    
    class Meta:
        model = apps.get_model('riders.Rider')      

        fields = ('rider_owner','team','bio','avatar_image','background_image','is_active','date_created','rate','kms_ceiling','kms_ridden')

        #'__all__'
    
    

class RiderDetailSerializer(RiderSerializer):
    donations = DonationSerializer(many=True, read_only=True)
    rider_updates = RiderUpdateSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.team = validated_data.get('team', instance.team)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.avatar_image = validated_data.get('avatar_image', instance.avatar_image)
        instance.background_image = validated_data.get('background_image', instance.background_image)
        instance.is_active = validated_data.get('is_active', instance.background_image)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.kms_goal = validated_data.get('kms_goal', instance.kms_goal)
        instance.rider_owner = validated_data.get('rider_owner', instance.rider_owner)
        instance.save()
        return instance
    
    class Meta:
        model = apps.get_model('riders.Rider')
        fields = '__all__'
    
