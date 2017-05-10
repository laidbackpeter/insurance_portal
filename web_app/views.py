# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

import datetime

# Create your views here.


def HomePageView(request):
    today = datetime.datetime.now().date()
    dayOfWeek = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
    return render(request, 'web_app/index.html', {'today': today, 'days_of_week': dayOfWeek})


def AboutPageView(request):
    return render(request, 'web_app/about.html', {})

