# Generated by Django 4.0.6 on 2024-07-19 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_customergooglelogin'),
        ('order', '0008_alter_orderdetails_modification'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.customer'),
        ),
    ]
