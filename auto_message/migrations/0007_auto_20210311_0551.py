# Generated by Django 3.1.5 on 2021-03-11 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_message', '0006_auto_20210305_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliocompany',
            name='commit_record',
            field=models.CharField(blank=True, default='', max_length=10000, null=True),
        ),
    ]
