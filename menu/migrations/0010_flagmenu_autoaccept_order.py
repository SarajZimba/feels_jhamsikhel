# Generated by Django 4.0.6 on 2024-07-25 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_remove_menutype_discount_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='flagmenu',
            name='autoaccept_order',
            field=models.BooleanField(default=False),
        ),
    ]
