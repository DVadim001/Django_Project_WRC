from django.shortcuts import render
from articles.models import Article


# Отображение главной страницы
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
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