# Generated by Django 4.0.6 on 2024-07-29 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=255, null=True),
        ),
    ]