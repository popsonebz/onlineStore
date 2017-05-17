from django.conf.urls import url, include
from . import views

app_name = 'AddressBookClient'

urlpatterns = [
                #url(r'^$', views.home, name='home'),
                url(r'^contact$', views.contact, name='contact',)
              ] 


