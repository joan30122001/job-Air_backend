from django.contrib import admin
from .models import Offer, UserOffer, Cv

# Register your models here.

admin.site.register(Offer)
admin.site.register(UserOffer)
admin.site.register(Cv)