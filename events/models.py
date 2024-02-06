from django.db import models


class Event(models.Model):
    event_title = models.CharField('Название события', max_length=256)
    event_text = models.TextField('Текст события')
    event_date = models.DateTimeField('Дата события')
    # Надо прикрепить фото события

    def __str__(self):
        return self.event_title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class Comment(models.Model):
    comment_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    comment_author_event = models.CharField('Автор комментария события', max_length=256)
    comment_text_event = models.TextField('Текст комментария события')
    comment_date_event = models.DateTimeField('Дата комментария события', auto_now_add=True)

    def __str__(self):
        return self.comment_author_event

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
