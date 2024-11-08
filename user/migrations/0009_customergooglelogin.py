# Generated by Django 4.0.6 on 2024-07-12 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_delete_customergooglelogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerGoogleLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(max_length=255, null=True)),
                ('google_id', models.CharField(max_length=200, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
