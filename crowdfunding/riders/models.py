from django.db import models
from django.db.models import Sum
from django.contrib.auth import get_user_model


class Rider(models.Model):
    
    rider_owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='user')
    team = models.CharField(max_length=200)
    bio = models.TextField(max_length=500)
    avatar_image = models.URLField()
    background_image = models.URLField()
    is_active = models.BooleanField()
    date_created = models.DateTimeField()
    kms_goal = models.IntegerField()
    # kms_ridden = models.IntegerField()
    @property
    def calc_kms_ridden(self):
        rider_updates = RiderUpdates.objects.select_related('rider').all()
        total_kms = rider_updates.aggregate(s=Sum('kms_ridden'))["s"]
        return(total_kms)
       


class RiderUpdates(models.Model):
    rider = models.ForeignKey('Rider', on_delete=models.CASCADE, related_name='rider_updates')
    kms_ridden = models.IntegerField(null=True)
    description = models.CharField(max_length=300)
    image = models.URLField()


class Donation(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    rider = models.ForeignKey('Rider',
                              on_delete=models.CASCADE,
                              related_name='donations')
    donor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='donor')

