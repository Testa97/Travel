# Generated by Django 4.2.2 on 2023-06-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_remove_prenotazione_metodo_pagamento_itinerario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itinerario',
            name='giorni',
        ),
        migrations.AddField(
            model_name='itinerario',
            name='day1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='itinerario',
            name='day2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='itinerario',
            name='day3',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='itinerario',
            name='day4',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='itinerario',
            name='day5',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='itinerario',
            name='day6',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='itinerario',
            name='day7',
            field=models.CharField(default='', max_length=200),
        ),
    ]
