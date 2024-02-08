from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('article/<int:pk>/', views.article, name='article_detail'),
    path('search/', views.search_article, name='search_article'),
    path('not_found/', views.article_not_found, name='article_not_found'),
    path('article/<int:pk>/comment/', views.comment, name='article_comment'),
    path('category/<int:category_id>/', views.articles_by_category, name='articles_by_category'),
]
