# Generated by Django 3.2.9 on 2021-12-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0025_auto_20211208_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trademodel',
            name='profit_loss',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
