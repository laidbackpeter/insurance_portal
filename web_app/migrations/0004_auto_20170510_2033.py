# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_auto_20170510_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_number',
            field=models.BigIntegerField(help_text='Enter identification number', primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
