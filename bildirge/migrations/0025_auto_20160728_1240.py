# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bildirge', '0024_auto_20160728_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='event',
            field=models.CharField(choices=[('GTZ', 'Genc Turkiye Zirvesi'), ('TR', 'Transist')], max_length=15, null=True),
        ),
    ]