# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import web_app.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_auto_20170510_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_num', models.CharField(help_text='Enter registration number of car with no spaces', max_length=20, validators=[web_app.fields.validate_lower])),
                ('desc', models.TextField(help_text='Enter brief description of car', max_length=200, validators=[web_app.fields.validate_lower])),
                ('model', models.TextField(help_text='Enter official model of car as per log book', max_length=200, validators=[web_app.fields.validate_lower])),
                ('year', models.IntegerField(help_text='Enter year of manufacture as per log book e.g. 2009', validators=[web_app.fields.validate_not_future])),
                ('processing_date', models.DateField(auto_now=True)),
                ('registration_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='registration_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, help_text='Enter identification number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='f_name',
            field=models.CharField(help_text='Enter first name of customer in lower caps', max_length=20, validators=[web_app.fields.validate_lower]),
        ),
        migrations.AlterField(
            model_name='user',
            name='m_name',
            field=models.CharField(help_text='Enter middle name of customer in lower caps', max_length=20, validators=[web_app.fields.validate_lower]),
        ),
        migrations.AlterField(
            model_name='user',
            name='s_name',
            field=models.CharField(help_text='Enter surname name of customer in lower caps', max_length=20, validators=[web_app.fields.validate_lower]),
        ),
        migrations.AddField(
            model_name='car',
            name='id_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.User'),
        ),
    ]
