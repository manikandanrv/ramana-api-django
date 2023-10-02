from sys import float_repr_style
from django.db import models
from iso3166 import countries

COUNTRY_CHOICES = sorted([(item[1],item[0]) for item in countries])
GUEST_HOUSES = [ ('K', 'Kurangu Thottam'),
                ('A', 'A Rooms'),
                ('AA', 'Achalam Guest House'),
                ('R', 'Post Office Rooms'),
                ('M', 'Mourvi Guest House')
                ]
VISA_TYPES = [('T','Tourist'), ('O','OCI'), ('e','eVisa')]
PURPOSES = [('T','Tourist'), ('E','Employment'), ('O','Other')]

class Devotee(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=70, blank=True, default='')
    last_name = models.CharField(max_length=70, blank=True, default='')
    email = models.CharField(max_length=70, blank=True, default='')
    mobile = models.CharField(max_length=70, blank=True, default='')
    aadhar_no = models.CharField(max_length=25, blank=True, default='')
    passport_no = models.CharField(max_length=25, blank=True, default='')
    address_building = models.CharField(max_length=50, blank=True, default='')
    address_doorno = models.CharField(max_length=15, blank=True, default='')
    address_line1 = models.CharField(max_length=50, blank=True, default='')
    address_line2 = models.CharField(max_length=50, blank=True, default='')
    address_city = models.CharField(max_length=50, blank=True, default='')
    address_state = models.CharField(max_length=50, blank=True, default='')
    address_country = models.CharField(choices=COUNTRY_CHOICES, default='India', max_length=50)
    nationality = models.CharField(choices=COUNTRY_CHOICES, default='India', max_length=50)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User',default=1, related_name='owner', on_delete=models.SET_DEFAULT)

    class Meta:
        ordering = ['created']

class Room(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    room_number = models.CharField(max_length=70, blank=True, default='')
    guesthouse_name = models.CharField(choices=GUEST_HOUSES, default='K', max_length=70, blank=True)
    room_type = models.CharField(max_length=70, blank=True, default='')
    max_guest_in_room = models.IntegerField( blank=True, default=2)
    is_room_booked = models.BooleanField(default=False)
    is_room_dirty = models.BooleanField(default=False)
    #house_keeping_instruction = models.CharField(max_length=50, blank=True, default='')
    #last_cleaned_date = models.CharField(max_length=15, blank=True, default='')
    #last_cleaned_by = models.CharField(max_length=50, blank=True, default='')
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

class Request(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    devotee = models.ForeignKey('Devotee',default=1,related_name='devotee',on_delete=models.SET_DEFAULT)
    likely_arrival = models.DateTimeField(auto_now_add=False)
    likely_departure = models.DateField(auto_now_add=False)
    no_of_guests = models.IntegerField( blank=True, default=1)
    purpose = models.CharField(max_length=200, blank=True, default='')
    is_request_approved = models.BooleanField(default=False)
    approver = models.ForeignKey('auth.User',default=1, related_name='approver', on_delete=models.SET_DEFAULT)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

class Checkin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    devotee = models.ForeignKey('Devotee',default=1,related_name='checkin_devotee',on_delete=models.SET_DEFAULT)
    checkin_date = models.DateTimeField(auto_now_add=True)
    likely_checkout_date = models.DateTimeField(auto_now_add=False)
    actual_checkout_date = models.DateTimeField(auto_now_add=False)
    no_of_guests = models.IntegerField( blank=True, default=1)
    purpose = models.CharField(max_length=200, blank=True, default='')
    rooms = models.ManyToManyField('Room')
    is_foreign_devotee = models.BooleanField(default=False)
    guests = models.ManyToManyField('Devotee')
    is_checkin_completed = models.BooleanField(default=False)
    is_checkout_completed = models.BooleanField(default=False)
    checkin_report_generated = models.BooleanField(default=False)
    checkout_report_generated = models.BooleanField(default=False)
    updated_by = models.ForeignKey('auth.User',default=1, related_name='updated_by', on_delete=models.SET_DEFAULT)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def checkout(self):
        return None

class ForeignDevotee(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    devotee = models.ForeignKey('Devotee',default=1,related_name='foreign_devotee',on_delete=models.CASCADE)
    first_name = models.CharField(max_length=70, blank=True, default='')
    last_name = models.CharField(max_length=70, blank=True, default='')
    email = models.CharField(max_length=70, blank=True, default='')
    mobile = models.CharField(max_length=70, blank=True, default='')
    passport_no = models.CharField(max_length=25, blank=True, default='')
    nationality = models.CharField(choices=COUNTRY_CHOICES, default='', max_length=50)
    passport_issue_city = models.CharField(max_length=25, blank=True, default='')
    passport_issue_country = models.CharField(choices=COUNTRY_CHOICES, default='', max_length=50)
    passport_issue_date = models.DateField(auto_now=False)
    passport_expiry_date = models.DateField(auto_now=float_repr_style)
    visa_no = models.CharField(max_length=25, blank=False, default='')
    visa_type = models.CharField(choices=VISA_TYPES, default='T', max_length=50)
    visa_issue_city = models.CharField(max_length=25, blank=False, default='')
    visa_issue_country = models.CharField(choices=COUNTRY_CHOICES, default='', max_length=50)
    visa_issue_date = models.DateField(auto_now=False)
    visa_valid_till = models.DateField(auto_now=False)
    purpose = models.CharField(choices=PURPOSES, default='T', max_length=50)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']



for item in countries:
    print(item)