from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

admin.site.register(Genre)
admin.site.register(Language)


# format of the book
class BooksInline(admin.TabularInline):
    model = Book


# admin model for the author
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


# book instance
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


# fields displayed in a list view
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


admin.site.register(Book, BookAdmin)


# admin model for book instance
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):

    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
