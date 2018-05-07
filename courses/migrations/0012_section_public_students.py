# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 13:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0011_auto_20180426_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='public_students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
