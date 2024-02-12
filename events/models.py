from django.db import models


# Таблица категорий новостей
class Category(models.Model):
    category_name_category = models.CharField(max_length=128)
    category_date_category = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name_category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Таблица событий
class Event(models.Model):
    event_to_category = models.ManyToManyField(Category, related_name='category_event', blank=True)
    event_title = models.CharField('Название события', max_length=256)
    event_text = models.TextField('Текст события')
    event_date = models.DateTimeField('Дата события',auto_now_add=True)
    # Надо прикрепить фото события

    def __str__(self):
        return self.event_title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


# Таблица комментариев для каждого события
class Comment(models.Model):
    comment_event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments_event')
    comment_author_event = models.CharField('Автор комментария события', max_length=256)
    comment_text_event = models.TextField('Текст комментария события')
    comment_date_event = models.DateTimeField('Дата комментария события', auto_now_add=True)

    def __str__(self):
        return self.comment_author_event

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
