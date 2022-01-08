# Generated by Django 3.2.9 on 2021-11-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0012_trademodel_tradingdaymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='trademodel',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name='tradingdaymodel',
            name='trades',
            field=models.ManyToManyField(to='sites.TradeModel'),
        ),
    ]
