# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from AddressBookClient.models import AddressBookTable

class AddressBookBackEndTestCase(TestCase):
    fixtures = ['test_contact.json']
    """docstring for AddressBookClientTestCase"""
    #Test if the url to view all contact works
    def test_openBackEndPage(self):
        resp = self.client.get("/addressbook-admin/all")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('addresses' in resp.context)

    #Test if the url to view the details of a record works
    def test_detail(self):
      resp = self.client.get('/addressbook-admin/details/1/')
      self.assertEqual(resp.status_code, 200)
      self.assertEqual(resp.context['contact'].pk, 1)
      self.assertEqual(resp.context['contact'].first_name, 'John')

      # Ensure that non-existent address throw a 404.
      resp = self.client.get('/addressbook-admin/details/50/')
      self.assertEqual(resp.status_code, 404)

    def test_edit(self):
      resp = self.client.get('/addressbook-admin/edit/1/')
      self.assertEqual(resp.status_code, 200)
      self.assertEqual(resp.context['contact'].pk, 1)
      self.assertEqual(resp.context['contact'].first_name, 'John')

      # Ensure that non-existent address throw a 404.
      resp = self.client.get('/addressbook-admin/edit/50/')
      self.assertEqual(resp.status_code, 404)


