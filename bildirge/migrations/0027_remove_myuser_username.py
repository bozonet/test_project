# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 12:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bildirge', '0026_remove_doc_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='username',
        ),
    ]
