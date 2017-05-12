# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse

from web_app.models import User, Car
import datetime

# Create your views here.


def HomePageView(request):
    today = datetime.datetime.now().date()
    dayOfWeek = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
    return render(request, 'web_app/index.html', {'today': today, 'days_of_week': dayOfWeek})


def AboutPageViewRedirect(request):
    return render(request, 'web_app/about.html', {})


def AboutPageView(request):
    return redirect(AboutPageViewRedirect)
    #return render(request, 'web_app/about.html', {})


def save_data(request):
    client_1 = User(f_name="jane", m_name="muthoni", s_name="muchina", id_number=12823982)

    client_1.save()

    # Read ALL entries
    objects = User.objects.all()
    res = 'Printing all User entries in the DB : <br>'

    for elt in objects:
        res += elt.f_name + "<br>"

    # Read a specific entry:
    sorex = User.objects.get(f_name="eva")
    res += 'Printing One entry <br>'
    res += sorex.f_name

    # Delete an entry
    res += '<br> Deleting an entry <br>'
    sorex.delete()

    # Update
    client_2 = User(f_name="charles", m_name="muchina", s_name="kanyi", id_number=12823982123)

    client_2.save()
    res += 'Updating entry<br>'

    client_2 = User.objects.get(f_name='thierry')
    client_2.f_name = 'eric'
    client_2.save()

    return HttpResponse(res)




