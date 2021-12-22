from django.contrib import admin
from .models import Post, PostImages,Textrow
import nested_admin

class PostImagesTextrowInline(nested_admin.NestedStackedInline):
    model = PostImages
    extra=0
    fk_name = 'level'

class TextrowInline(nested_admin.NestedStackedInline):
    model= Textrow
    extra=0
    fk_name = 'level'

    inlines=[PostImagesTextrowInline]

class PostAdmin(nested_admin.NestedModelAdmin):
    model= Post
    inlines = [TextrowInline]
    list_display = ('id', 'title')

admin.site.register(Post, PostAdmin)
