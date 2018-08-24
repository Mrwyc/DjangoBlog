from django.contrib import admin
from blog.models import BlogsPost, BlogCtg


# Register your models here.



class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'timestamp', 'category']


class CaTeGory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(BlogsPost, BlogsPostAdmin)
admin.site.register(BlogCtg, CaTeGory)