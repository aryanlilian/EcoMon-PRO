from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'published_date', 'updated_date']


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'posted_date', 'updated_date']
