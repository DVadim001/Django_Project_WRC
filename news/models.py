from django.db import models


# Таблица категорий новостей
class Category(models.Model):
    category_name_news = models.CharField(max_length=128)
    category_date_news = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name_news


# Таблица новостей
class News(models.Model):
    news_to_category = models.ManyToManyField(Category, blank=True, related_name='category_news')
    news_title = models.CharField('Название новости', max_length=256)
    news_text = models.TextField('Текст новости')
    news_date = models.DateTimeField('Дата публикации новости', auto_now_add=True)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


# Таблица комментариев для каждой новости
class Comment(models.Model):
    comment_news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments_news')
    comment_author_news = models.CharField('Автор комментария новости', max_length=256)
    comment_text_news = models.TextField('Текст комментария новости')
    comment_date_news = models.DateTimeField('Дата комментария новости', auto_now_add=True)

    def __str__(self):
        return self.comment_author_news

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
