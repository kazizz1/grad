from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id','username', 'email','password','is_active']


class UserPasswordSerializers(serializers.ModelSerializer):
    new_password = serializers.CharField(required=True, write_only=True)

    class Meta(object):
        model = User
        fields = ['email','password', 'new_password']


class UserListSerializers(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'email', 'is_active']  
            