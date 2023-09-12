from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth import get_user_model



class Rider(models.Model):

    class KmsToDollar(models.IntegerChoices):
        KM_1 = 1, '1km'
        KM_2 = 2, '2km'
        KM_5 = 5, '5km'
    
    rider = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='user')
    team = models.CharField(max_length=200)
    bio = models.TextField(max_length=500)
    avatar_image = models.URLField(default='https://picsum.photos/200?grayscale')
    background_image = models.URLField(default='https://picsum.photos/1000/160?grayscale')
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    rate = models.PositiveIntegerField(choices=KmsToDollar.choices, default=KmsToDollar.KM_1, help_text="How may kms would you like to ride for each $ donated?")
    kms_ceiling = models.IntegerField(default=400)
   
    @property
    def kms_ridden(self):
        return self.updates.all().aggregate(total=Sum('kms_ridden'))['total']
    
    @property
    def amount_donated(self):
        return(self.donations.all().aggregate(total=Sum('amount'))['total'])
    
    @property
    def kms_to_ride(self):
        if self.amount_donated:
            return(self.rate * self.amount_donated)
        else:
            return(None)


class RiderUpdates(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='updates')
    kms_ridden = models.IntegerField(null=True)
    description = models.CharField(max_length=300)
    image = models.URLField(default='https://picsum.photos/200?grayscale')


class Donation(models.Model):
    amount = models.IntegerField(default=0)
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField(default=False)
    rider = models.ForeignKey(Rider,
                              on_delete=models.CASCADE,
                              related_name='donations')
    donor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='donor')

