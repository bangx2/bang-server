from django.db import models
from account.models import User


class Bang(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    members = models.ManyToManyField(User, related_name="bangs")
    owner = models.ForeignKey(User, related_name="own_bangs")

    bang_id = models.CharField(max_length=32)
