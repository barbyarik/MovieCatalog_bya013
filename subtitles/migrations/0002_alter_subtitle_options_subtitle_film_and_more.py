# Generated by Django 5.1.3 on 2024-12-03 20:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
        ('subtitles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subtitle',
            options={'ordering': ['film', 'start_time'], 'verbose_name': 'Субтитр', 'verbose_name_plural': 'Субтитры'},
        ),
        migrations.AddField(
            model_name='subtitle',
            name='film',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='films.film', verbose_name='Фильм'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subtitle',
            name='end_time',
            field=models.FloatField(verbose_name='Время окончания (сек.)'),
        ),
        migrations.AlterField(
            model_name='subtitle',
            name='start_time',
            field=models.FloatField(verbose_name='Время начала (сек.)'),
        ),
        migrations.AlterField(
            model_name='subtitle',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]