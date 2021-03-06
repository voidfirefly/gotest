# Generated by Django 2.0.3 on 2018-05-12 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_auto_20180512_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='testlog',
            name='appointed_test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tests.AppointedTest', verbose_name='Назначение'),
        ),
        migrations.AddField(
            model_name='testlog',
            name='available_test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tests.AvailableTest', verbose_name='Доступ'),
        ),
    ]
