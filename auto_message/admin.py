from django.contrib import admin
from .models import PortfolioCompany


class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'fund', 'name', 'investment_manager', 'contact', 'position', 'phone', 'email', 'cycle', 'status', 'active')
    search_fields = ('name', 'fund', 'name', 'investment_manager', 'contact', 'position', 'phone',)


admin.site.register(PortfolioCompany, PortfolioAdmin)
