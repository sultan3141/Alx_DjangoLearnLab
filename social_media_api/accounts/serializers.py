from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        # include the fields you want to allow during registration
        fields = ("username", "email", "password", "bio", "profile_picture")

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        # Optionally create token automatically on registration:
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data.get("username"), password=data.get("password"))
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        data["user"] = user
        return data

class UserSerializer(serializers.ModelSerializer):
    # for profile display / update
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "bio", "profile_picture", "followers", "following")
        read_only_fields = ("followers", "following")
