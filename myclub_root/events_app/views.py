from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import date
import calendar
from calendar import HTMLCalendar
from .models import Event
from .forms import VenueForm


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
    template = 'events_app/calendar_base.html'
    return render(request, template, context_dict)


def all_events(request):
    event_list = Event.objects.all()
    template = 'events_app/event_list.html'
    context_dict = {'event_list': event_list}
    return render(request, template, context_dict)


def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue/?submitted=True')
    else:
        form = VenueForm()
        print('request ---->', request)
        print('request.GET --->', request.GET)
        print('request.POST --->', request.POST)
        if 'submitted' in request.GET:
            submitted = True
    template = 'events_app/add_venue.html'
    form_dict = {'form': form, 'submitted': submitted}
    return render(request, template, form_dict)
