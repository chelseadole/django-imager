# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-01 20:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0005_auto_20171201_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
