from django.contrib import admin

from .models import Item, MarketingCampaign, User, get_items


admin.site.register(Item)
admin.site.register(MarketingCampaign)
admin.site.register(User)
