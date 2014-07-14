from rest_framework import serializers
from .models import Bang


class BangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bang
