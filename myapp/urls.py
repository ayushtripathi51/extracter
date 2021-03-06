from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls import urls as polls_urls
from home import urls as home_urls
import home.views
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home.views.index, name='index'),	
    url(r'^polls/',include(polls_urls)),
    url(r'^admin/', include(admin.site.urls)),
)
