# Generated by Django 4.0.6 on 2024-07-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_outlet'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='accepted_time',
            field=models.CharField(max_length=100, null=True),
        ),
    ]