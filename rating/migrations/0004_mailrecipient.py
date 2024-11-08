# Generated by Django 4.0.6 on 2024-07-24 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0003_tblratings_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailRecipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
