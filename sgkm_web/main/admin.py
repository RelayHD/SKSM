from django.contrib import admin
from .models import Post, PostImages,Textrow
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
import nested_admin

#앨범객체를 보여줄 때 객체에 연결된 사진객체를 같이 보여주기 위해서 세로로 나열되게 지정(TabularInline은 행으로 나열)
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

# @admin.register(PostImages)
# class PostImagesAdmin(nested_admin.NestedModelAdmin):
#     list_display = ('id', 'post')
#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)
#         for img in request.FILES.getlist('photos'):
#             obj.productimage_set.create(image_url=img)

# @admin.register(Textrow)
# class PostTextrowAdmin(nested_admin.NestedModelAdmin):
#     list_display = ('id', 'post')
#     def save_model(self, request, obj, form, change):
#             super().save_model(request, obj, form, change)
    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)
    #     for text in request.FILES.getlist('photos'):
    #         obj.productimage_set.create(image_url=img)