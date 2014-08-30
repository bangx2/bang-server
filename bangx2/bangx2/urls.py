from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bangx2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',\
        namespace='rest_framework')),
    url(r'^api-token-auth/',\
        'rest_framework.authtoken.views.obtain_auth_token'),

    url(r'^bang/', include('bang.urls')),
    url(r'^survey/', include('survey.urls')),
)
