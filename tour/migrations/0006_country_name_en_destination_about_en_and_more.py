# Generated by Django 4.2.7 on 2023-12-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0005_remove_country_name_en_remove_destination_about_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='name_en',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='about_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='city_en',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='includeexclude',
            name='name_en',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='duration_en',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='itinerary_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='overview_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='title_en',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
