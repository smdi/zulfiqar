# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-30 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutepro', '0005_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_no', models.CharField(max_length=30)),
                ('block_name', models.CharField(max_length=30)),
                ('street_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
    ]
