# Generated by Django 4.0.6 on 2024-07-23 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_flagmenu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menutype',
            name='discount_percentage',
        ),
    ]
