from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contacts', views.contact, name='contact'),
    url(r'^roles', views.role, name='role'),
    url(r'^details', views.detail, name='detail'),
]
