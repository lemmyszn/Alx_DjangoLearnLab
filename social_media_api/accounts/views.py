# accounts/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserRegistrationSerializer
from rest_framework.permissions import AllowAny

class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # Use the serializer to validate and save the data
        response = super().create(request, *args, **kwargs)
        user = response.data
        token = Token.objects.get(user_id=user['id'])

        # Return the user data along with the token
        return Response({
            'user': user,
            'token': token.key
        })
