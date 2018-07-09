from django.conf.urls import url
from django.conf.urls import patterns,include,url

from . import views


urlpatterns = [
    url(r'roles/$', views.role, name='uliza-role'),
    url(r'roles/add/$', views.add_role, name='add_role'),
    url(r'details/$', views.detail, name='uliza-detail'),
    url(r'details/add/$', views.add_detail, name='add_detail'),
    url(r'contacts/$', views.contact, name='uliza-contact'),
    url(r'contacts/add/$', views.add_contact, name='add_contact'),
]

