from django.contrib import admin

# Register your models here.
from booklib.models import Genre, Author, Book, BookInstance

admin.site.register(Genre)


# Define the admin class

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')

# Register the admin class with the associated model
# admin.site.register(Book, AuthorAdmin)

# Register the Admin classes for Book using using a decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'display_genre')

# Register the Admin classes for BookInstance using using a decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    pass