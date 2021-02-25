from django.db import models


class PortfolioCompany(models.Model):
    name = models.CharField(max_length=50, null=True)
    principal = models.CharField(max_length=10, null=True)
    tele_number = models.CharField(max_length=11, null=True)
    cycle = models.CharField(max_length=10, null=True, choices=(('monthly', 'monthly'), ('quarter', 'quarter')))
    status = models.BooleanField(null=True, default=False)

    class Meta:
        ordering = ["name"]

    def __bool__(self):
        return self.status

