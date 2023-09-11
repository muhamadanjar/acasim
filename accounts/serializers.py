from accounts.models import User, Profile
from django.contrib.auth.models import Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Profile
        fields = ("user", )
