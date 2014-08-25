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
    end_time = models.DateTimeField(null=False, blank=False)

    public = models.BooleanField(default=False)
    notify = models.BooleanField(default=True)
    only_invitee = models.BooleanField(default=True)

    # id of survey schema in mongo
    schema = models.CharField(max_length=20, null=False, blank=False)
    # id of result doccument in mongo
    result = models.CharField(max_length=20, null=False, blank=False)

    invitee = models.ManyToManyField(User, through="InviteeShip")


class SurveyResult(models.Model):
    answerer = models.ForeignKey(User, related_name="answered_surveys")
    modify_time = models.DateTimeField(null=False, blank=False,\
            default=datetime.now())


class InviteeShip(models.Model):
    survey = models.ForeignKey(Survey)
    invitee = models.ForeignKey(User)
    submit = models.BooleanField(default=False)
