from rest_framework import serializers
from .models import Bang
# from account.models import User

# class MemberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'alias')

class BangSerializer(serializers.ModelSerializer):
    # members = MemberSerializer(many=True)

    class Meta:
        model = Bang
        fields = ('name', 'description', 'bang_id', 'members', 'owner')
