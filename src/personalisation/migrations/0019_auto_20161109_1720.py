# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-09 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalisation', '0018_segment_visit_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='segment',
            name='disable_date',
            field=models.DateField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='enable_date',
            field=models.DateField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='segment',
            name='visit_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
