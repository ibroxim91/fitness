# Generated by Django 4.1.7 on 2024-01-05 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_tariff_alter_admin_options_alter_admin_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariff',
            name='name_en',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tariff',
            name='name_ru',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tariff',
            name='name_uz',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tariff',
            name='text_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tariff',
            name='text_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tariff',
            name='text_uz',
            field=models.TextField(blank=True, null=True),
        ),
    ]
