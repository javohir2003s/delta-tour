# Generated by Django 4.2.7 on 2023-12-07 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_post_body_en_post_title_en'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_en',
        ),
    ]
