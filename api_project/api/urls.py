from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Ensure this is correct
]
from django.urls import path
from .views import BookList  # Ensure this is from the correct module

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
   
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]
