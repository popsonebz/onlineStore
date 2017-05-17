# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.core.urlresolvers import reverse

from .form import AddressBookForm
# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = AddressBookForm(request.POST)

        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return  redirect('AddressBookClient:contact')

    else:
        form = AddressBookForm()
    return render(request, 'addressBookClient/addressbook.html', {'form':form})
