from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    """(Venue description)"""
    name = models.CharField('Venue Name', blank=True, max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip', blank=True, max_length=300)
    phone = models.CharField(blank=True, max_length=100)
    web = models.URLField('Web Address', blank=True)
    email_address = models.EmailField('Email', blank=True)

    def __str__(self):
        name = self.name
        return name


class MyClubUser(models.Model):
    """(MyCLubUser description)"""
    first_name = models.CharField(blank=True, max_length=100)
    last_name = models.CharField(blank=True, max_length=100)
    email_address = models.EmailField('Email')

    def __str__(self):
        first_name = self.first_name
        last_name = self.last_name
        return "{}, {}".format(first_name, last_name)


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(
        Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    attendees = models.ManyToManyField(MyClubUser, blank=True)
    description = models.TextField(blank=True)

    def event_timing(self, date):
        if self.event_date > date:
            return "Event is after this date"
        elif self.event_date == date:
            return "Event is on the same day"
        else:
            return "Event is before this date"

    @property
    def name_slug(self):
        return self.name.lower().replace(' ','-')

    def __str__(self):
        name = self.name
        return name
