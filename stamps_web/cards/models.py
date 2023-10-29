from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone

from companies.models import Company


class CardType(models.Model):
    name = models.CharField(max_length=100)
    # foreign keys
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

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
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    card_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    card_type = models.ForeignKey(CardType, on_delete=models.CASCADE, null=True)
    # dates
    start_date = models.DateTimeField(default=timezone.now)
    used_date = models.DateTimeField(blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    # stamps collecting logic
    collected_stamps = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.card_owner.username} card of {self.company}'
