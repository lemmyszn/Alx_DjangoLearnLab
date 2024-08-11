
from django.contrib import admin
from .models import Book
from django.db import models


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    # Display fields in the list view
    list_display = ('title', 'author', 'published_date', 'isbn', 'pages')

  # Enable search functionality
    search_fields = ('title', 'author', 'isbn')
    
    # Add filters for published date and author
    list_filter = ('published_date', 'author')
    
    # Optionally, you can configure ordering
    ordering = ('-published_date',)
    
    # Configure which fields to display in the detail view
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'published_date', 'isbn', 'pages', 'cover')
        }),
    )

    # Configure which fields to display in the form
    formfield_overrides = {
        models.CharField: {'widget': admin.widgets.AdminTextInputWidget}, 
    }