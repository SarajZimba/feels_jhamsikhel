# Generated by Django 4.0.6 on 2024-07-23 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0009_remove_menutype_discount_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('sorting_order', models.IntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('date', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('outlet', models.CharField(blank=True, max_length=20, null=True)),
                ('table_no', models.IntegerField(null=True)),
                ('atmosphere_rating', models.FloatField()),
                ('service_rating', models.FloatField()),
                ('presentation_rating', models.FloatField()),
                ('cleanliness_rating', models.FloatField()),
                ('overall_rating', models.FloatField()),
                ('review', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tblitemRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('sorting_order', models.IntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('rating', models.FloatField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('itemId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menu')),
                ('tblrating', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rating.tblratings')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
