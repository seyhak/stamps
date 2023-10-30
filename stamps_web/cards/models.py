from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models

from companies.models import Company


class CardType(models.Model):
    name = models.CharField(max_length=100)
    # foreign keys
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    maximum_stamps = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(
                20,
                'maximum amount of stamps is too big'
            )
        ]
    )


class Card(models.Model):
    # foreign keys
    card_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    card_type = models.ForeignKey(CardType, on_delete=models.CASCADE, null=False, blank=False)
    # dates
    start_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    used_date = models.DateTimeField(blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    # stamps collecting logic
    collected_stamps = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.card_owner.username} card of type {self.card_type.name}'
