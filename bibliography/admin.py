from models import Book, BookCategory
from django.contrib import admin


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_as_text', 'publication_as_text',
                    'category', 'discipline')

admin.site.register(BookCategory)
admin.site.register(Book, BookAdmin)
