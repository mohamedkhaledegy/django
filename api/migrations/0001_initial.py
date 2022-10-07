# Generated by Django 3.2.16 on 2022-10-07 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fix_request', to=settings.AUTH_USER_MODEL)),
                ('fix_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='repair_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
