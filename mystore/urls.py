from django.conf.urls import url, include
from . import views

app_name = 'mystore'

urlpatterns = [
                url(r'^$', views.home, name='home'),
              ]
#python2 manage.py shell
#from django.core.urlresolvers import *
#resolve("/mystore/")
# result :  ResolverMatch(func=mystore.views.home, args=(), kwargs={}, url_name=home, app_names=['mystore'], namespaces=['mystore'])


#reverse('mystore:home')
#result:  '/mystore/'

