from django.contrib import admin

from .models import Book, Author

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name ', 'last_name')

admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_bestseller', 'rating')
    list_display = ('title', 'author')

admin.site.register(Book, BookAdmin)