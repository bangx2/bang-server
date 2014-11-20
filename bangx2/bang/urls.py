#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from bang import views


urlpatterns = patterns(
    'bang.views',

#     url(r'^bangs/$', views.BangList.as_view()),
#     url(r'^bangs/(?P<pk>[0-9]+)/$', views.BangDetail.as_view()),

    url(r'^default-bang/$', 'get_default_bang'),
    url(r'^my-bangs/$', 'get_my_bangs'),
    url(r'^create-bang/$', 'create_bang'),
    url(r'^quit-bang/$', 'quit_bang'),
    url(r'^bang-detail/$', 'get_bang_detail'),
    url(r'^bang-members/$', 'get_bang_members'),

    url(r'^bang-logo-uptoken/(?P<bang_id>[\w-]+)/$',\
        'get_bang_logo_uptoken'),

)

