# Generated by Django 4.1.3 on 2022-11-25 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('StocksData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valuation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_cap', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pe_ratio', models.FloatField()),
                ('symbol_key', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='symbol_key', to='StocksData.stocks')),
            ],
        ),
    ]
