# Generated by Django 2.0.3 on 2018-06-16 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0008_auto_20180526_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestKlassDepence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Класс вопроса',
                'verbose_name_plural': 'Классы вопросов',
            },
        ),
        migrations.CreateModel(
            name='TestKlassDepenceItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klass', models.CharField(blank=True, max_length=255, null=True, verbose_name='Класс вопроса')),
                ('count', models.PositiveSmallIntegerField(default=0)),
                ('test_klass_depence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.TestKlassDepence', verbose_name='Настройка классов вопроса')),
            ],
        ),
        migrations.AlterField(
            model_name='test',
            name='estimate_method',
            field=models.CharField(choices=[('default', 'Стандартный'), ('many_answers', 'Множество ответов'), ('klass_depence', 'Классовый подбор')], max_length=50, verbose_name='Метод оценки'),
        ),
        migrations.AddField(
            model_name='appointedtest',
            name='test_klass_depence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tests.TestKlassDepence', verbose_name='Настройка классов вопроса'),
        ),
        migrations.AddField(
            model_name='availabletest',
            name='test_klass_depence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tests.TestKlassDepence', verbose_name='Настройка классов вопроса'),
        ),
    ]
