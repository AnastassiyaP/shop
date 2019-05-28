import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser as DjangoAbstractUser


class Item(models.Model):
    dttm_created = models.DateTimeField(default=datetime.datetime.now)
    dttm_deleted = models.DateTimeField(null=True, blank=True)

    price = models.FloatField()
    name = models.CharField(max_length=16, default='', blank=True)
    details = models.CharField(max_length=1024, null=True, blank=True)



class MarketingCampaign(models.Model):
    dttm_created = models.DateTimeField(default=datetime.datetime.now)
    dttm_deleted = models.DateTimeField(null=True, blank=True)

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
    campaign = models.ForeignKey(MarketingCampaign, on_delete=models.CASCADE, null=True, blank=True)
    bought_items = models.ManyToManyField(Item)



from django.db.models import Count, Sum, Q

def get_items(sex, price):
    qs = Item.objects
    f = Q(user__date_joined__lt='2019-05-01')

    if sex:
        sex_filter = Q(user__sex=sex)
        f &= sex_filter
        qs = qs.filter(sex_filter)

    if price:
        qs = qs.filter(price__lte=price)
    return qs.annotate(count=Count('user', filter=f))

def get_user_boughts(id):
    return User.objects.filter(id__in=id).annotate(
        bought_item_count=Count('bought_items'),
        bought_item_price=Sum('bought_items__price'))
