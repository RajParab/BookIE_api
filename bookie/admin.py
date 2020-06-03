from django.contrib import admin
from .models import Book, Chapter
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('title',)}
	list_filter=['genre','rating']



@admin.register(Chapter)
class BookAdmin(admin.ModelAdmin):
	list_filter=['bookName']
