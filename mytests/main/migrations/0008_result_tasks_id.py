# Generated by Django 4.2.7 on 2023-12-07 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_result_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='tasks_id',
            field=models.TextField(default=False),
        ),
    ]
