# Generated by Django 4.0.6 on 2024-07-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_orderdetails_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='modification',
            field=models.CharField(max_length=200, null=True),
        ),
    ]