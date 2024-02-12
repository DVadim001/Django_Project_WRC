from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import News, Category
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


# Вывод всех новостей на основной странице по новостям
def main_news(request):
    search = forms.SearchForm()
    news = News.objects.order_by('-news_date')
    context = {'search': search, 'news': news}
    return render(request, 'news/news_list.html', context)


# Вывод новостей по определённой категории
def news_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    news = category.category_news.all()
    return render(request, 'news/news_by_category.html', {'category': category, 'news': news})


# Вывод отдельной конкретной новости
def news(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    comments = news_item.comments_news.order_by('-id')
    if request.method == 'POST':
        # Создаём экземпляр формы и заполняем его данными из запроса:
        comment_form = forms.CommentForm(request.POST)
        # Проверяем валидность формы:
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # Сразу в БД не сохраняем
            comment.news = news_item # Привязываем комментарий к конкретной новости
            comment.save() # Теперь сохраняем
            return redirect('news:news_detail', pk=news_item.pk) # Перенаправляем обратно к новости
    else:
        comment_form = forms.CommentForm() # Создаём пустой экземпляр формы для GET-запроса

    # Добавляем форму комментария в текст
    context = {'news': news_item,
               'comments': comments,
               'comment_form': comment_form}
    return render(request, 'news/news.html', context)


# Поиск новостей по фильтру
def search_news(request):
    if 'search_query' in request.GET:
        search_query = request.GET.get('search_query')
        news = News.objects.filter(news_title__icontains=search_query)
        if news: # Проверяет, содержит ли запрос объекты
            # Если новости найдены, рендер страницы с результатами поиска
            context = {'news': news}
            return render(request, 'news/search_result.html', context)
        else:
            # Если новости не найдены, перенаправляем на страницу "not found"
            return redirect('news:not_found')


# Оставление комментария на стр определённой новости зарегистрированным пользователем
@login_required
def comment(request, pk):
    news_item = News.objects.filter(pk=pk).first()
    if not news_item:
        raise Http404('Новость не найдена.')

    if request.method == "POST":
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.comment_news = news_item  # Устанавливаем связь с новостью правильно
            comment.save()
            return HttpResponseRedirect(reverse('news:news_detail', args=[news_item.pk,]))
    return HttpResponseRedirect(reverse('news:news_detail', args=[news_item.pk,]))


# Если не найдено, то редирект на "не найдено"
def news_not_found(request):
    return render(request, 'news/not_found.html')

