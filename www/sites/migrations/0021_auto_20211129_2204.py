# Generated by Django 3.2.9 on 2021-11-29 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0020_auto_20211129_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_quote', models.CharField(max_length=12)),
                ('stock', models.CharField(max_length=24)),
                ('stock_amount', models.PositiveIntegerField()),
                ('entry_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('exit_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_commision', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='TradingDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trading_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AddField(
            model_name='trademodel',
            name='trading_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.tradingday'),
        ),
    ]
