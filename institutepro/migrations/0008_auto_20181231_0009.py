# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-30 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutepro', '0007_auto_20181230_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackdata',
            name='feedback',
            field=models.CharField(max_length=2000),
        ),
    ]
