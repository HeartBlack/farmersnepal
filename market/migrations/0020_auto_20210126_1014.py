# Generated by Django 3.1.5 on 2021-01-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0019_auto_20210126_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='deliveryCharge',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
