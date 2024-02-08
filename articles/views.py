from django.shortcuts import render, redirect
# from . import forms
from .models import Article, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View

from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from django.http import HttpResponse

from django.shortcuts import get_object_or_404




# Вывод всех статей

# Вывод статей по определённой категории
def articles_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    articles = category.category_article.all()
    context = {'category': category, 'articles': articles}
    return render(request, 'articles_by_category.html', context)


# Вывод отдельной конкретной статьи
def article(request,pk):
    try:
        a = Article.objects.get(id=pk)
    except:
        raise Http404('К сожалению, новость не найдена')
    comments = a.comments.order_by('-id')
    context = {'article': a, 'comments': comments}
    return render(request, 'article.html', context)


# Поиск статей по фильтру
def search_article(request):
    if request.method == 'POST':
        get_article = request.POST.get('search_article')
        articles = Article.objects.filter(article_title__icontains=get_article)
        if articles: # Проверяет, содержит ли запрос объекты
            # Если статьи найдены, рендер страницы с результатами поиска
            context = {'articles': articles}
            return render(request, 'search_result.html', context)
        else:
            # Если статьи ненайдены, перенаправляем на страницу "not found"
            return redirect('/not_found')


# Оставление комментария на стр определённой статьи
def comment(request, pk):
    try:
        comm = Article.objects.get(id=pk)
    except:
        raise Http404('Статья не найдена.')
    comm.comments.create(comment_author_article=request.POST['name'], comment_text_article=request.POST['text'])
    return HttpResponseRedirect(reverse('articles:article_detail', args=(comm.id,)))


# Если не найдено, то редирект на "не найдено"
def article_not_found(request):
    return render(request, 'not_found.html')



#
#
#
#
#
#
#
#
#



