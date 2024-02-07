from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.article, name='article_detail')

]