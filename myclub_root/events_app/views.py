from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar


def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 2000 or year > 2099:
        year = date.today().year
    month_name = calendar.month_name[month]
    title = "MyClub Event Calendar - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    mensaje = title
    context_dict = {'title': mensaje, 'cal': cal}
    template = 'base.html'
    return render(request, template, context_dict)
