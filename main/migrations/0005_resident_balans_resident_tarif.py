# Generated by Django 5.0.1 on 2024-01-15 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_tariff_name_en_tariff_name_ru_tariff_name_uz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='balans',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resident',
            name='tarif',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.tariff'),
        ),
    ]
