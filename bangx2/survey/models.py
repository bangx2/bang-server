from django.db import models
from account.models import User
from bang.models import Bang
from datetime import datetime


class Survey(models.Model):
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=1000, null=True, blank=True)

    owner = models.ForeignKey(User, related_name="own_surveys")
    bang = models.ForeignKey(Bang, related_name="own_surveys")

    create_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    # visible to all bang(survey and result)
    is_public = models.BooleanField(default=False)
    # notify invitee who is not answer survey before end_time
    need_notify = models.BooleanField(default=True)
    # only invitee can answer this survey
    is_invitee_only = models.BooleanField(default=True)

    # id of survey schema in mongo
    schema = models.CharField(max_length=20, null=True, blank=True)

    invitee = models.ManyToManyField(User, through="InviteeShip")


class SurveyResult(models.Model):
    answerer = models.ForeignKey(User, related_name="answered_results")
    survey = models.ForeignKey(Survey, related_name="answered_results")

    # id of result doccument in mongo
    result = models.CharField(max_length=20, null=False, blank=False)

    modify_time = models.DateTimeField(null=False, blank=False,\
            default=datetime.now())


class InviteeShip(models.Model):
    survey = models.ForeignKey(Survey)
    invitee = models.ForeignKey(User)
    is_submitted = models.BooleanField(default=False)
    # survey_result = models.ForeignKey(User, null=True, blank=True)
