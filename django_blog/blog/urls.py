from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import add_comment, search_posts, TaggedPostListView,PostDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView, PostByTagListView

urlpatterns = [
    # Post-related URLs
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comment-related URLs
    path('post/<int:post_id>/comments/new/', add_comment, name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
    path('post/<int:pk>/comments/new/'),
    # Authentication URLs
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Tag and Search-related URLs
    path('search/', search_posts, name='search'),
    path('tags/<str:tag_name>/', TaggedPostListView.as_view(), name='tag_posts'),

      # URL pattern to filter posts by tags
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
]
