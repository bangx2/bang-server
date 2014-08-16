#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from bang import views


urlpatterns = patterns(
    'bang.views',

#     url(r'^bangs/$', views.BangList.as_view()),
#     url(r'^bangs/(?P<pk>[0-9]+)/$', views.BangDetail.as_view()),

    url(r'^my-bangs/$', 'get_my_bangs'),
    url(r'^create-bang/$', 'create_bang'),
    url(r'^quit-bang/(?P<bang_id>[0-9]+)/$', 'quit_bang'),
    url(r'^bang-detail/(?P<bang_id>[0-9]+)/$', 'get_bang_detail'),
    url(r'^bang-members/(?P<bang_id>[0-9]+)/$', 'get_bang_members'),

)


