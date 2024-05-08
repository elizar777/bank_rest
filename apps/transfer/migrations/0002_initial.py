# Generated by Django 5.0.4 on 2024-05-08 13:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transfer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='historytransfer',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfers_sent', to=settings.AUTH_USER_MODEL, verbose_name='От пользователя'),
        ),
        migrations.AddField(
            model_name='historytransfer',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfers_received', to=settings.AUTH_USER_MODEL, verbose_name='К пользователю'),
        ),
    ]
