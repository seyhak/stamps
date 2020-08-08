from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(
        max_length=250, blank=False,
        null=False, unique=True
    )
    date_added = models.DateTimeField(default=timezone.now)

    company_logo_url = models.CharField(
        max_length=1000,
        default='https://interactive-examples.mdn.mozilla.net/media/examples/grapefruit-slice-332-332.jpg'
    )
    company_stamp_url = models.CharField(
        max_length=1000,
        default='http://www.pngall.com/wp-content/uploads/2016/07/Sun-Download-PNG.png'
    )
    company_background_image_url = models.CharField(
        max_length=1000, null=True, blank=True
    )   

    company_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
