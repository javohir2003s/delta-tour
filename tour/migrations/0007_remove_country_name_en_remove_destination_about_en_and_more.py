# Generated by Django 4.2.7 on 2023-12-07 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0006_country_name_en_destination_about_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='about_en',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='city_en',
        ),
        migrations.RemoveField(
            model_name='includeexclude',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='duration_en',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='itinerary_en',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='overview_en',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='title_en',
        ),
    ]
