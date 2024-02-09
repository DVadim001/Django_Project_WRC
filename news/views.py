from django.shortcuts import render, redirect
# from . import forms
from .models import News, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View

from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from django.http import HttpResponse

from django.shortcuts import get_object_or_404


# Вывод всех новостей

# Вывод новостей по определённой категории
def news_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    news = category.category_news.all()
    context = {'category': category, 'news': news}
    return render(request, 'news_by_category.html', context)


# Вывод отдельной конкретной новости
def news(request,pk):
    try:
        a = News.objects.get(id=pk)
    except:
        raise Http404('К сожалению, новость не найдена')
    comments = a.comments.order_by('-id')
    context = {'news': a, 'comments': comments}
    return render(request, 'news/news.html', context)


# Поиск новостей по фильтру
def search_news(request):
    if request.method == 'POST':
        get_news = request.POST.get('search_news')
        news = News.objects.filter(news_title__icontains=get_news)
        if news: # Проверяет, содержит ли запрос объекты
            # Если статьи найдены, рендер страницы с результатами поиска
            context = {'news': news}
            return render(request, 'search_result.html', context)
        else:
            # Если статьи ненайдены, перенаправляем на страницу "not found"
            return redirect('/not_found')


# Оставление комментария на стр определённой новости
def comment(request, pk):
    try:
        comm_n = News.objects.get(id=pk)
    except:
        raise Http404('Новость не найдена.')
    comm_n.comments_n.create(comment_author_news=request.POST['name'], comment_text_news=request.POST['text'])
    return HttpResponseRedirect(reverse('news:news_detail', args=(comm_n.id,)))


# Если не найдено, то редирект на "не найдено"
def news_not_found(request):
    return render(request, 'not_found.html')

