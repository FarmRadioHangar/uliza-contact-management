from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'contactmanager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include('contacts.urls', namespace='uliza-contacts', app_name='contacts')),
    url(r'^', include('contacts.urls')),
]
