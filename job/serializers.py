from job.models import Cv
from .models import Offer, UserOffer, Cv
from user.models import User
from rest_framework import serializers

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = [
            'id',
            'title',
            'domain',
            'region',
            'description',
            'begin_date',
            'end_date',
            'user',
        ]


class UserOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOffer
        fields = [
            'id',
            'offer',
            'user',
        ]



class CvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cv
        fields = [
            'id',
            'document',
            'user',
        ]