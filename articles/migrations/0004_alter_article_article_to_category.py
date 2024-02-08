# Generated by Django 5.0.1 on 2024-02-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_article_to_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_to_category',
            field=models.ManyToManyField(blank=True, related_name='category_article', to='articles.category'),
        ),
    ]