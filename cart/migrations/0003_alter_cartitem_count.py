# Generated by Django 4.2.7 on 2023-12-04 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cartitem_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
