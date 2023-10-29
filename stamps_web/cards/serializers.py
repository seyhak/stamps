from cards.models import Card, CardType
from rest_framework import serializers


class CardTypeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardType
        fields = [
            'name', 'maximum_stamps', 'company'
        ]


class CardTypeSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name')
    created_by = serializers.CharField(source='created_by.username')

    class Meta:
        model = CardType
        fields = [
            'name', 'company_name',  'created_by',
            'maximum_stamps', 'created_at'
        ]


class CardSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name')
    company_logo_url = serializers.CharField(source='company.company_logo_url')
    company_stamp_url = serializers.CharField(source='company.company_stamp_url')
    company_background_image_url = serializers.CharField(source='company.company_background_image_url')

    class Meta:
        model = Card
        fields = [
            'company_name', 'company_logo_url',  'company_stamp_url',
            'company_background_image_url', 'card_owner', 'start_date', 'used_date',
            'expiration_date', 'collected_stamps'
        ]
