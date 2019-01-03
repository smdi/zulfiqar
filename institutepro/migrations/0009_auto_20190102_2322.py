# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-02 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutepro', '0008_auto_20181231_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackdata',
            name='datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='username',
            field=models.TextField(max_length=20, unique=True),
        ),
    ]
