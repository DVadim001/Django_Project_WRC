from django.shortcuts import render
from articles.models import Article
from news.models import News


# Отображение главной страницы
def index(request):
    articles = Article.objects.all() # получаем все статьи
    news = News.objects.all() # получаем все новости
    context = {'articles': articles, 'news': news}
    return render(request, 'main/index.html', context)


# Отображение страницы О нас
def about(request):
    return render(request, 'main/about.html')


# Отображение страницы Наши партнёры
def partners(request):
    return render(request, 'main/partners.html')

# Регистрация
# Функция выхода
#
#