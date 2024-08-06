from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from base.models import User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not (username or email):
            raise serializers.ValidationError("Must include 'username' or 'email'")
        if not password:
            raise serializers.ValidationError("Must include 'password'")

        # Authenticate using either username or email
        user = None
        if username:
            user = authenticate(username=username, password=password)
        elif email:
            try:
                user = authenticate(username=User.objects.get(email=email).username, password=password)
            except User.DoesNotExist:
                raise serializers.ValidationError("Invalid email")

        if user:
            if not user.is_active:
                raise serializers.ValidationError("User is deactivated")
            return user
        else:
            raise serializers.ValidationError("Unable to log in with provided credentials")

    def create(self, validated_data):
        user = validated_data
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        }
