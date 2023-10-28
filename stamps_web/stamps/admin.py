from django.contrib import admin

from cards.models import Card
from companies.models import Company


@admin.register(Card)
class CardsAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'start_date', 'used_date')
    search_fields = [
        'company__id', 'company__name',
        'user__id', 'user__username',
        'start_date', 'used_date'
    ]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_added')
    search_fields = [
        'company__id', 'company__name', 'date_added'
    ]
