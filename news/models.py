from django.db import models


class News(models.Model):
    news_title = models.CharField('Название новости', max_length=256)
    news_text = models.TextField('Текст новости')
    news_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    comment_news = models.ForeignKey(News, on_delete=models.CASCADE)
    comment_author_news = models.CharField('Автор комментария новости', max_length=256)
    comment_text_news = models.TextField('Текст комментария новости')
    comment_date_news = models.DateTimeField('Дата комментария новости', auto_now_add=True)

    def __str__(self):
        return self.comment_author_news

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
