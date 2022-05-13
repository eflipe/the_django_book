from django.db import models


class Venue(models.Model):
    """(Venue description)"""
    name = models.CharField('Venue Name', blank=True, max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip', blank=True, max_length=300)
    phone = models.CharField(blank=True, max_length=100)
    web = models.URLField('Web Address')
    email_address = models.EmailField('Email')

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
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=60)
    attendees = models.ManyToManyField(MyClubUser, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        name = self.name
        return name
