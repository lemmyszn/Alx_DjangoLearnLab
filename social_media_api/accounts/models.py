from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Create a through model to handle the following relationship
    following = models.ManyToManyField('self', through='Follow', symmetrical=False, related_name='followers')

    def __str__(self):
        return self.username

class Follow(models.Model):
    # Defines the follow relationship with explicit foreign keys
    user = models.ForeignKey(CustomUser, related_name='following_relations', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(CustomUser, related_name='follower_relations', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'followed_user')

    def __str__(self):
        return f"{self.user.username} follows {self.followed_user.username}"
