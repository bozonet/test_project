# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 08:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bildirge', '0021_contact_user_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='cinsiyet',
        ),
    ]
