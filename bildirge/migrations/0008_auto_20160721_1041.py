# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 07:41
from __future__ import unicode_literals

import bildirge.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bildirge', '0007_auto_20160721_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='upload',
            field=models.FileField('profile/%Y/%m/%d'),
        ),
    ]
