from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import News, Category, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.http import Http404, HttpResponseRedirect, HttpResponse
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
    context = {'category': category, 'news': news}
    return render(request, 'news_by_category.html', context)


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
    if request.method == 'POST':
        get_news = request.POST.get('search_news')
        news = News.objects.filter(news_title__icontains=get_news)
        if news: # Проверяет, содержит ли запрос объекты
            # Если новости найдены, рендер страницы с результатами поиска
            context = {'news': news}
            return render(request, 'search_result.html', context)
        else:
            # Если новости не найдены, перенаправляем на страницу "not found"
            return redirect('/not_found')


# Оставление комментария на стр определённой новости
# def comment(request, pk):
#     try:
#         comm_n = News.objects.get(id=pk)
#     except:
#         raise Http404('Новость не найдена.')
#     comm_n.comments_news.create(comment_author_news=request.POST['name'], comment_text_news=request.POST['text'])
#     return HttpResponseRedirect(reverse('news:news_detail', args=(comm_n.id,)))


def comment(request, pk):
    news_item = get_object_or_404(News, pk)
    if request.method == "POST":
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.comment_news = news_item
            comment.save()
            return HttpResponseRedirect(reverse('news:news_detail', args=(news_item.pk,)))
    return HttpResponseRedirect(reverse('news:news_detail', args=(news_item.pk,)))


# Если не найдено, то редирект на "не найдено"
def news_not_found(request):
    return render(request, 'not_found.html')

