import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser as DjangoAbstractUser


class Item(models.Model):
    dttm_created = models.DateTimeField(default=datetime.datetime.now)
    dttm_deleted = models.DateTimeField()

    price = models.FloatField()
    name = models.CharField(max_length=16, default='', blank=True)
    details = models.CharField(max_length=1024, null=True, blank=True)



class MarketingCampaign(models.Model):
    dttm_created = models.DateTimeField(default=datetime.datetime.now)
    dttm_deleted = models.DateTimeField()

    dttm_start = models.DateTimeField()
    dttm_end = models.DateTimeField()

    name = models.CharField(max_length=16, )


class User(DjangoAbstractUser):
    SEX_FEMALE = 'F'
    SEX_MALE = 'M'
    SEX_CHOICES = (
        (SEX_FEMALE, 'Female',),
        (SEX_MALE, 'Male',),
    )

    sex = models.CharField(max_length=1,  choices=SEX_CHOICES)
    campaign = models.ForeignKey(MarketingCampaign, on_delete=models.CASCADE)
    bought_items = models.ManyToManyField(Item)



from django.db.models import Count
def get_items():
    return Item.objects.filter(
        user__sex='F',
        user__campaign__name='t'
    ).annotate(
        count=Count('id'),
    ).distinct('id'),
