# Generated by Django 4.2.7 on 2023-12-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Комментарий'),
        ),
    ]