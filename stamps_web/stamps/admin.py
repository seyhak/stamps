from django.contrib import admin

from companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "date_added")
    search_fields = ["company__id", "company__name", "date_added"]
