# Generated by Django 4.0.6 on 2024-07-25 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_billrequest_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('sorting_order', models.IntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('outlet', models.CharField(blank=True, max_length=100, null=True)),
                ('table', models.IntegerField()),
                ('hash_value', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
