# Generated by Django 3.1.5 on 2021-02-02 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliocompany',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
