from django.conf.urls import url, include
from .views import address_list, details, edit, delete

app_name = 'AddressBookBackEnd'

urlpatterns = [
                url(r'^all$', address_list, name='address_list',),
                url(r'^details/(?P<address_id>[0-9]+)/$', details, name='details',),
                url(r'^edit/(?P<address_id>[0-9]+)/$', edit, name='edit',),
                url(r'^delete/(?P<address_id>[0-9]+)/$', delete, name='delete',),
                
              ]


