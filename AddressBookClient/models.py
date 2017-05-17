# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.validators import RegexValidator
# Create your models here.
class AddressBookTable(models.Model):
    #alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    alphabet = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabet characters are allowed.')
    first_name = models.CharField(max_length=100, validators=[alphabet])
    last_name = models.CharField(max_length=100, validators=[alphabet])
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: 999999999 or +123344455 . minimum of 9 and maximum of 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=False, max_length=15, unique=True, error_messages={'unique':"This phone number already exist for a user."})
    email_address = models.EmailField(blank=False, null=False)
    address = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.first_name 
