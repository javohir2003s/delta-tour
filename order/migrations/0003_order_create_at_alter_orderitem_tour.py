# Generated by Django 4.2.7 on 2023-12-04 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_remove_tour_discount_price_alter_tourimg_tour'),
        ('order', '0002_alter_orderitem_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitem', to='tour.tour'),
        ),
    ]
