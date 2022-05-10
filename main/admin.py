from django.contrib import admin
from .models import Book, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','pub_date')
    search_fields = ['title','description']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)