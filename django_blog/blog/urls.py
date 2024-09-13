from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path("post/<int:pk>/delete/","post/<int:pk/update/","post/new/"),
    path("post/<int:pk>/update/"),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/',views.register, name='register'),
    path('profile/', views.profile, name='profile'),

]

from django.urls import path
from .views import add_comment, CommentUpdateView, CommentDeleteView ,CommentCreateView

urlpatterns = [
    path('post/<int:post_id>/comments/new/', add_comment, name='add-comment'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='update-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    
]
