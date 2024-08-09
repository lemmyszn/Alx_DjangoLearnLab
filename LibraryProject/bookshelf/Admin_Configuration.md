# Admin Interface Configuration for Book Model

## Registering the Book Model

In `bookshelf/admin.py`, register the `Book` model to make it manageable through the Django admin interface:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn', 'pages')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('published_date', 'author')
    ordering = ('-published_date',)
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'published_date', 'isbn', 'pages', 'cover')
        }),
    )
    formfield_overrides = {
        models.CharField: {'widget': admin.widgets.AdminTextInputWidget},
    }
