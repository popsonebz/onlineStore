# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from AddressBookClient.models import AddressBookTable

from AddressBookClient.form import AddressBookForm

from django.http import Http404

from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url="/login")
def address_list(request):
    addresses = AddressBookTable.objects.all().order_by('first_name')
    return render(request, 'addressBookBackEnd/index.html', {'addresses': addresses})

def details(request, address_id):
    try:
        contact = AddressBookTable.objects.get(pk=address_id)
    except AddressBookTable.DoesNotExist:
        raise Http404("Address does not exist")

    else:
        return render(request, 'addressBookBackEnd/details.html', {'contact': contact})
def edit(request, address_id):
    try:
        contact = AddressBookTable.objects.get(pk=address_id)
    except AddressBookTable.DoesNotExist:
        raise Http404("Address does not exist")

    if request.method == 'POST':
        form = AddressBookForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
        return  redirect('AddressBookBackEnd:address_list') 
    else:
	    return render(request, 'addressBookBackEnd/edit.html', {'contact': contact}) 

def delete(request, address_id):
    try:
        address = AddressBookTable.objects.get(pk=address_id)
        address.delete()
    except AddressBookTable.DoesNotExist:
        raise Http404("Address does not exist")
    return  redirect('AddressBookBackEnd:address_list')
