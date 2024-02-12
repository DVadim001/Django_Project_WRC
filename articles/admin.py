from django.contrib import admin
from django import forms
from .models import Article, Comment, Category
from ckeditor.widgets import CKEditorWidget


# Форма для модели Article с интеграцией CKEditor
class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'  # Используем все поля модели
        widgets = {
            'content': CKEditorWidget(),  # 'content' - поле, которое будет редактироваться через CKEditor
        }


# Класс для настройки интерфейса модели Article в админ-панели
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm


# Регистрация модели Article с настройками из ArticleAdmin
admin.site.register(Article, ArticleAdmin)

# Регистрация других моделей без специальных настроек
admin.site.register(Comment)
admin.site.register(Category)
