from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^helloworld$', 'djevelskap.base.views.helloworld'),
    url(r'^list_all$', 'djevelskap.base.views.list_all'),
    url(r'^list_all_tpl$', 'djevelskap.base.views.list_all_tpl'),
    url(r'^delivery/(?P<id>\d+)?$', 'djevelskap.base.views.restful_delivery')
    # url(r'^djevelskap/', include('djevelskap.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
