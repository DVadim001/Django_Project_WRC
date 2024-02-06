# Generated by Django 5.0.1 on 2024-02-06 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=256, verbose_name='Название события')),
                ('event_text', models.TextField(verbose_name='Текст события')),
                ('event_date', models.DateTimeField(verbose_name='Дата события')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author_event', models.CharField(max_length=256, verbose_name='Автор комментария события')),
                ('comment_text_event', models.TextField(verbose_name='Текст комментария события')),
                ('comment_date_event', models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария события')),
                ('comment_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
