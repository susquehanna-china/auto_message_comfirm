from django.db import models


class PortfolioCompany(models.Model):
    fund = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    investment_manager = models.CharField(max_length=50, null=True, blank=True)
    contact = models.CharField(max_length=10, null=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    cycle = models.CharField(max_length=10, null=True, choices=(('monthly', 'monthly'), ('quarter', 'quarter')))
    status = models.BooleanField(null=True, default=False)
    active = models.BooleanField(null=True, default=True)
    commit_record = models.CharField(max_length=10000, null=True, blank=True, default=' ')
    comment = models.TextField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __bool__(self):
        return self.status

