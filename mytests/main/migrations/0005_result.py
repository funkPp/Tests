# Generated by Django 4.2.7 on 2023-12-01 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_alter_tasks_order_with_respect_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата теста')),
                ('tr', models.IntegerField(verbose_name='Количество правильных ответов')),
                ('fs', models.IntegerField(verbose_name='Количество неправильных ответов')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.tests')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результаты',
            },
        ),
    ]