# Generated by Django 4.0.6 on 2024-08-14 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_remove_customer_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
