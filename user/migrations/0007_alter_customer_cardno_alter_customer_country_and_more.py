# Generated by Django 4.0.6 on 2024-07-11 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cardNo',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='vatNo',
            field=models.CharField(max_length=255, null=True),
        ),
    ]