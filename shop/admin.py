from django.contrib import admin
from .models import Book,Author,Category

# Register your models here.
@ admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'describe', 'author', 'category', 'year', 'photo')
    list_filter = ('author','category')


@ admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@ admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}
