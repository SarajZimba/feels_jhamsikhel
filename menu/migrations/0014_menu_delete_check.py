# Generated by Django 4.0.6 on 2024-08-14 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_alter_mediafile_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='delete_check',
            field=models.BooleanField(default=True),
        ),
    ]
