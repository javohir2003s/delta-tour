# Generated by Django 4.2.7 on 2023-12-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
