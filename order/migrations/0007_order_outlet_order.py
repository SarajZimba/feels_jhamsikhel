# Generated by Django 4.0.6 on 2024-07-11 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_orderdetails_modification'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='outlet_order',
            field=models.IntegerField(null=True),
        ),
    ]
