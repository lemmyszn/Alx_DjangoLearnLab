from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .serializers import UserRegistrationSerializer, UserSerializer, PostSerializer
from .models import CustomUser, Post, Follow
from rest_framework.permissions import IsAuthenticated


# Helper function for token generation
def generate_token_response(user):
    token, created = Token.objects.get_or_create(user=user)
    return {
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email
        },
        'token': token.key
    }

# User registration view
class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(id=response.data['id'])
        return Response(generate_token_response(user))

# Custom token authentication view
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return Response(generate_token_response(user))

# Follow/Unfollow user (combine both actions)
class FollowUnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id, *args, **kwargs):
        user_to_follow = get_object_or_404(CustomUser, pk=user_id)
        if request.user == user_to_follow:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        Follow.objects.get_or_create(user=request.user, followed_user=user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)

    def delete(self, request, user_id, *args, **kwargs):
        user_to_unfollow = get_object_or_404(CustomUser, pk=user_id)
        follow_relation = Follow.objects.filter(user=request.user, followed_user=user_to_unfollow)

        if follow_relation.exists():
            follow_relation.delete()
            return Response({"message": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)
        return Response({"error": "You are not following this user."}, status=status.HTTP_400_BAD_REQUEST)

# List all users
class ListUsersView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

# User feed view
class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
