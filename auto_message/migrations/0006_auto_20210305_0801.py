# Generated by Django 3.1.5 on 2021-03-05 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto_message', '0005_auto_20210305_0745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfoliocompany',
            old_name='principal',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='portfoliocompany',
            old_name='tele_number',
            new_name='phone',
        ),
    ]
