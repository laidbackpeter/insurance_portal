# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from web_app.fields import validate_lower, validate_not_future

from django.contrib import admin

# Create your models here.
#User info

class User(models.Model):

    f_name = models.CharField(max_length=20, null=False, blank=False, validators=[
        validate_lower], help_text="Enter first name of customer in lower caps")
    m_name = models.CharField(max_length=20, null=False, blank=False, validators=[
        validate_lower], help_text="Enter middle name of customer in lower caps")
    s_name = models.CharField(max_length=20, null=False, blank=False, validators=[
        validate_lower], help_text="Enter surname name of customer in lower caps")
    id_number = models.BigIntegerField(blank=False, null=False, unique=True, primary_key=True, help_text="Enter identification number")
    registration_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'tbl_users'


class Car(models.Model):
    reg_num = models.CharField(max_length=20, null=False, blank=False, validators=[
        validate_lower],  help_text="Enter registration number of car with no spaces")
    desc = models.TextField(max_length=200,  help_text="Enter brief description of car", validators=[
        validate_lower])
    model = models.TextField(max_length=200,  help_text="Enter official model of car as per log "
                                                        "book", validators=[
        validate_lower])
    year = models.IntegerField(null=False, blank=False, validators=[
        validate_not_future], help_text="Enter year of manufacture as per log book e.g. 2009")
    processing_date = models.DateField(auto_now=True)
    registration_date = models.DateField(auto_now_add=True)
    id_number = models.ForeignKey(User, on_delete=models.CASCADE)

