from django.contrib import admin

from .models import Blog, Category, Tag


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "author", "created_time",
                    "modified_time")
    ordering = ("-modified_time", )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Tag)
class TagAmin(admin.ModelAdmin):
    list_display = ("id", "name")