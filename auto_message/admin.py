from django.contrib import admin
from .models import PortfolioCompany


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'principal', 'tele_number', 'status')
    search_fields = ('name',)


admin.site.register(PortfolioCompany, PortfolioAdmin)

