# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-26 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20170426_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.IntegerField(default=3),
        ),
    ]