from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('news/<int:pk>/', views.news, name='news_detail'),
    path('search/', views.search_news, name='search_news'),
    path('not_found/', views.news_not_found, name='news_not_found'),
    path('news/<int:pk>/comment/', views.comment, name='news_comment'),
    path('category/<int:category_id>/', views.news_by_category, name='news_by_category'),
]
