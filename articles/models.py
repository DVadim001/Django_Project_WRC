from django.db import models
from ckeditor.fields import RichTextField


# Таблица категорий статей
class Category(models.Model):
    category_name = models.CharField(max_length=128)
    category_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Таблица статей
class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=256)
    content = RichTextField('')
    article_to_category = models.ManyToManyField(Category, blank=True, related_name='category_article')
    # article_text = models.TextField('Текст статьи')
    article_date = models.DateTimeField('Дата публикации статьи', auto_now_add=True)

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


# Таблица комментариев для каждой статьи
class Comment(models.Model):
    comment_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment_author_article = models.CharField('Автор комментария статьи', max_length=256)
    comment_text_article = models.TextField('Текст комментария статьи')
    comment_date_article = models.DateTimeField('Дата комментария статьи', auto_now_add=True)

    def __str__(self):
        return self.comment_author_article

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
