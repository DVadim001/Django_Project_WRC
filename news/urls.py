from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.main_news, name='news_list'),
    path('<int:pk>/', views.news, name='news_detail'),
    path('search/', views.search_news, name='search_news'),
    path('not_found/', views.news_not_found, name='news_not_found'),
    path('<int:pk>/comment/', views.comment, name='news_comment'),
    path('category/<int:category_id>/', views.news_by_category, name='news_by_category'),
]
