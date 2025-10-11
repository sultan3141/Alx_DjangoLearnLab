from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "bio", "profile_picture")

    def create(self, validated_data):
        password = validated_data.pop("password")
        # Use the manager’s create_user method to ensure proper handling
        user=get_user_model().objects.create_user(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
            password=password,
            bio=validated_data.get("bio", ""),
            profile_picture=validated_data.get("profile_picture", None),
        )
        # Optionally automatically generate a token
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data.get("username"),
            password=data.get("password")
        )
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        data["user"] = user
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "bio", "profile_picture", "followers", "following")
        read_only_fields = ("followers", "following")
