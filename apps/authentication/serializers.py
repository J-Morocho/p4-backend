from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    # Serialize password field
    password = serializers.CharField(
        max_length=255,
        min_length=8,
        write_only=True
    )

    # User is not allowed to change the JWT token
    token = serializers.CharField(max_length=255, read_only=True)

    # Specify the model to serialize
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',
                  'password', 'token')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255, read_only=True)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'token')

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)
        # raise exception on blank username
        if username is None:
            raise serializers.ValidationError(
                'username required to login'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to login'
            )

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with that username or password was not found'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )
        return {
            'username': user.username,
            'email': user.email,
            'token': user.token
        }

# TODO: Figure out what this is doing


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
