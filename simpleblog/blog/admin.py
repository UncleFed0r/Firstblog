from django.contrib import admin
from django.contrib.auth.models import User

from .models import Tag, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    save_as = True


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    save_as = True

