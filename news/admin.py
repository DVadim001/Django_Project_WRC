from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.News)
admin.site.register(models.Comment)
admin.site.register(models.Category)
