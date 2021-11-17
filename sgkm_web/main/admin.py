from django.contrib import admin
from .models import Post, PostImages

#앨범객체를 보여줄 때 객체에 연결된 사진객체를 같이 보여주기 위해서 세로로 나열되게 지정(TabularInline은 행으로 나열)
class PostImagesInline(admin.StackedInline):
    model = PostImages

@admin.register(Post)#데코레이터 장점 : 간편함.
class PostAdmin(admin.ModelAdmin):
    inlines = (PostImagesInline,)#앨범 객체 수정 화면을 보여줄 때 PhotoInline에서 정의한 사항을 보여줌.
    list_display = ('id', 'title')

@admin.register(PostImages)
class PostImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'post')
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        for img in request.FILES.getlist('photos'):
            obj.productimage_set.create(image_url=img)