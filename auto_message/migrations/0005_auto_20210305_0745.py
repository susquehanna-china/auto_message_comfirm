# Generated by Django 3.1.5 on 2021-03-05 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_message', '0004_portfoliocompany_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliocompany',
            name='commit_record',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='portfoliocompany',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='portfoliocompany',
            name='fund',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='portfoliocompany',
            name='investment_manager',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='portfoliocompany',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
