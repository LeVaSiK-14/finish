from django.contrib.auth.models import User
from .models import UserOneC
from rest_framework import serializers


class UserOneCListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOneC
        fields = ['usernameforonec', 'passwordforonec', 'wayforbd', 'userid']

