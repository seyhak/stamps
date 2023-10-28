from cards.models import Card
from rest_framework import serializers


class CardSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name')
    company_logo_url = serializers.CharField(source='company.company_logo_url')
    company_stamp_url = serializers.CharField(source='company.company_stamp_url')
    company_background_image_url = serializers.CharField(source='company.company_background_image_url')

    class Meta:
        model = Card
        fields = [
            'company_name', 'company_logo_url',  'company_stamp_url',
            'company_background_image_url', 'user', 'start_date', 'used_date',
            'expiration_date', 'collected_stamps', 'maximum_stamps'
        ]
