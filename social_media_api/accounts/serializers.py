# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import CustomUser

# Get the user model (CustomUser in your case)
User = get_user_model().objects.create_user

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Use CharField for password (write-only to ensure it's not included in output)
    password = serializers.CharField()
class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'bio', 'profile_picture')

    def create(self, validated_data):
        """
        Custom method to create a user with the hashed password and generate a token.
        """
        # Use create_user() to handle password hashing
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],  # Password will be hashed here
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )

        # Automatically create an authentication token for the new user
        Token.objects.create(user=user)

        return user
