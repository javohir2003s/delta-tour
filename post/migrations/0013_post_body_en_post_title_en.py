# Generated by Django 4.2.7 on 2023-12-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_remove_post_i18n_post_body_ru_post_body_uz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
