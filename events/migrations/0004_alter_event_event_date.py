# Generated by Django 5.0.1 on 2024-02-11 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата события'),
        ),
    ]