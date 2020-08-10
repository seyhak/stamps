from cards.models import Card
from rest_framework import serializers


class CardSerializer(serializers.ModelSerializer):
    company_logo_url = serializers.CharField(source='company.company_logo_url')

    class Meta:
        model = Card
        fields = [
            'company_logo_url', 'user', 'start_date',
            'used_date', 'expiration_date', 'collected_stamps',
            'maximum_stamps'
        ]
