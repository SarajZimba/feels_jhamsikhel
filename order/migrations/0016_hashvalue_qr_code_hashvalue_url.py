# Generated by Django 4.0.6 on 2024-09-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_order_billreqwithdiscount_order_discounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashvalue',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr/'),
        ),
        migrations.AddField(
            model_name='hashvalue',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
