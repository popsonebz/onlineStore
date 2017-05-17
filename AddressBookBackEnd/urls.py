from django.conf.urls import url, include
from . import views

app_name = 'AddressBookBackEnd'

urlpatterns = [
                url(r'^all$', views.address_list, name='address_list',),
                url(r'^details/(?P<address_id>[0-9]+)/$', views.details, name='details',),
                url(r'^edit/(?P<address_id>[0-9]+)/$', views.edit, name='edit',),
                url(r'^delete/(?P<address_id>[0-9]+)/$', views.delete, name='delete',) 
              ]


