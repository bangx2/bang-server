from django.db import models


class Bang(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    create_time = models.DateTimeField(auto_now_add=True)
