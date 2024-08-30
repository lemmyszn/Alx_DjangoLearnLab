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
