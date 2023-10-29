from django.contrib import admin
from cards.models import Card


# Register your models here.
@admin.register(Card)
class CardsAdmin(admin.ModelAdmin):
    list_display = ('card_owner', 'company', 'start_date', 'used_date')
    search_fields = [
        'company__id', 'company__name',
        'user__id', 'user__username',
        'start_date', 'used_date'
    ]
