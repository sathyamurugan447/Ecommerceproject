# Generated by Django 3.1.4 on 2020-12-05 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_e_commerce', '0003_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
