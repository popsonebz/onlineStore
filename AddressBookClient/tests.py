# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from AddressBookClient.models import AddressBookTable

from AddressBookClient.form import AddressBookForm

class AddressBookClientTestCase(TestCase):
    fixtures = ['test_contact.json']
    """docstring for AddressBookClientTestCase"""
    
    # The tests if we can access the link for adding contact
    def test_openClientPage(self):
        resp = self.client.get("/addressbook/contact")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('form' in resp.context)
    
    # This should succeed when the inputs are correct
    def test_valid_address_entery(self):
        form = AddressBookForm({
        'first_name': "Turanga",
        'last_name': "felix",
        'phone_number' : "082346123509",
        'email_address': "leela@example.com",
        'address': "park lanne",
        })
        self.assertTrue(form.is_valid())
        address = form.save()
        self.assertEqual(address.first_name, "Turanga")
        self.assertEqual(address.last_name, "felix")
        self.assertEqual(address.email_address, "leela@example.com")
        self.assertEqual(address.phone_number, "082346123509")
        self.assertEqual(address.address, "park lanne")

    #This should fail when the data is empty
    def test_blank_data(self):
        form = AddressBookForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'first_name': ['required'],
            'last_name': ['required'],
            'email_address': ['required'],
            'phone_number': ['required'],
            })
