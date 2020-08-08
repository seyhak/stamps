from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone

from companies.models import Company


class Card(models.Model):
    # foreign keys
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # dates
    start_date = models.DateTimeField(default=timezone.now)
    used_date = models.DateTimeField(blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    # stamps collecting logic
    collected_stamps = models.PositiveSmallIntegerField(default=0)
    maximum_stamps = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(
                20,
                'maximum amount of stamps is too big'
            )
        ]
    )

    def __str__(self):
        return f'{self.user.username} card of {self.company}'
