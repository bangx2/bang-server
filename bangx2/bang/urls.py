#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from bang import views


urlpatterns = patterns(
    'bang.views',

    url(r'^bangs/$', views.BangList.as_view()),
    url(r'^bangs/(?P<pk>[0-9]+)/$', views.BangDetail.as_view()),
)


