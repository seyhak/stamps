from rest_framework import serializers

from cards.models import Card, CardType


class CardTypeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardType
        fields = ["name", "maximum_stamps", "company"]


class CardTypeSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source="company.name")
    created_by = serializers.CharField(source="created_by.username")

    class Meta:
        model = CardType
        fields = ["name", "company_name", "created_by", "maximum_stamps", "created_at"]


class CardCreateSerializer(serializers.ModelSerializer):
    def get_card_owner(self):
        return self.context["request"].user

    def create(self, validated_data):
        card_owner = self.get_card_owner()
        data = {**validated_data, **{"card_owner": card_owner}}
        return super().create(data)

    class Meta:
        model = Card
        fields = [
            "card_type",
        ]


class CardSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source="card_type.company.name")
    company_logo_url = serializers.CharField(
        source="card_type.company.company_logo_url"
    )
    company_stamp_url = serializers.CharField(
        source="card_type.company.company_stamp_url"
    )
    company_background_image_url = serializers.CharField(
        source="card_type.company.company_background_image_url"
    )

    class Meta:
        model = Card
        fields = [
            "id",
            "company_name",
            "company_logo_url",
            "company_stamp_url",
            "company_background_image_url",
            "card_owner",
            "start_date",
            "expiration_date",
            "expiration_date",
            "collected_stamps",
            "updated_at",
        ]
