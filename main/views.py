from django.shortcuts import render, redirect
from .forms import SignUpForm

from articles.models import Article
from news.models import News
from events.models import Event


# Отображение главной страницы
def index(request):

    # Переписать!!!
    articles = Article.objects.all() # получаем все статьи
    news = News.objects.all() # получаем все новости
    events = Event.objects.all() # Получаем все события
    context = {'articles': articles,
               'news': news,
               'events': events}
    return render(request, 'main/index.html', context)


# Отображение страницы О нас
def about(request):
    return render(request, 'main/about.html')


# Отображение страницы Наши партнёры
def partners(request):
    return render(request, 'main/partners.html')

# Регистрация
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    else:
        form = SignUpForm()
        context = {'form': form}
    return render(request, 'main/signup.html', context)


# Функция выхода
