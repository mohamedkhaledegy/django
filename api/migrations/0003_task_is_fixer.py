# Generated by Django 3.2.16 on 2022-10-07 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_fixer',
            field=models.BooleanField(default=False, verbose_name='Fixer'),
        ),
    ]
