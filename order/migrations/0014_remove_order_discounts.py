# Generated by Django 4.0.6 on 2024-09-02 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_hashvalue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discounts',
        ),
    ]