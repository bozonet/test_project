# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 14:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bildirge', '0032_auto_20160728_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='user',
            field=models.ForeignKey(blank=True, default='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]