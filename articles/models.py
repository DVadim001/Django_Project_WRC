from django.db import models


class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=256)
    article_text = models.TextField('Текст статьи')
    article_date = models.DateTimeField('Дата публикации статьи')

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    comment_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment_author_article = models.CharField('Автор комментария', max_length=256)
    comment_text_article = models.TextField('Текст комментария')
    comment_date_article = models.DateTimeField('Дата комментария статьи', auto_now_add=True)

    def __str__(self):
        return self.comment_author_article

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
