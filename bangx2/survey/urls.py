#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from survey import views


urlpatterns = patterns(
    'survey.views',

    url(r'^created-surveys-within-bang/$', 'get_created_surveys_within_bang'),
    url(r'^create-survey/$', 'create_survey'),

)


