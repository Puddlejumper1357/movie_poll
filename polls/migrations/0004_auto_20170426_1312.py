# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-26 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170426_0606'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='movies',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]