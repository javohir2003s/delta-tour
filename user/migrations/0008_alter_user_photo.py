# Generated by Django 4.2.7 on 2023-12-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='/static/user_image/default.jpg', upload_to='user_image/'),
        ),
    ]