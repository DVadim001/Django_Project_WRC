from django.contrib import admin
from .models import Image, Comment, Category


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'upload_date')
    list_filter = ('upload_date', 'category')
    search_fields = ('title', 'description')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created_date', 'image')
    search_fields = ('text', 'author__username')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Image, ImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)


