from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Article, Category
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


# Вывод всех статей на основной странице по статьям
def main_article(request):
    search = forms.SearchForm()
    articles = Article.objects.order_by('-article_date')
    context = {'search': search, 'articles': articles}
    return render(request, 'articles/article_list.html', context)


# Вывод статей по определённой категории
def articles_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    articles = category.category_article.all()
    context = {'category': category, 'articles': articles}
    return render(request, 'articles/articles_by_category.html', context)


# Вывод отдельной конкретной статьи
def article(request, pk):
    article_item = get_object_or_404(Article, pk=pk)
    comments = article_item.comments.order_by('-id')
    if request.method == 'POST':
        # Создаём экземпляр формы и заполняем его данными из запроса:
        comment_form = forms.CommentForm(request.POST)
        # Проверяем валидность формы:
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # Сразу в БД не сохраняем
            comment.article = article_item # Привязываем комментарий к конкретной новости
            comment.save() # Теперь сохраняем
            return redirect('articles:article_detail', pk=article_item.pk) # Перенаправляем обратно к новости
    else:
        comment_form = forms.CommentForm() # Создаём пустой экземпляр формы для GET-запроса

    # Добавляем форму комментария в текст
    context = {'article': article_item,
               'comments': comments,
               'comment_form': comment_form}
    return render(request, 'articles/article.html', context)


# Поиск статей по фильтру
def search_article(request):
    if 'search_article' in request.GET:
        get_article = request.GET.get('search_article')
        articles = Article.objects.filter(article_title__icontains=get_article)
        if articles: # Проверяет, содержит ли запрос объекты
            # Если статьи найдены, рендер страницы с результатами поиска
            context = {'articles': articles}
            return render(request, 'articles/search_result.html', context)
        else:
            # Если статьи не найдены, перенаправляем на страницу "not found"
            return redirect('articles:article_not_found')


# Оставление комментария на стр определённой статьи зарегистрированным пользователем
@login_required
def comment(request, pk):
    article_item = Article.objects.filter(pk=pk).first()
    if not article_item:
        raise Http404('Статья не найдена.')
    if request.method == "POST":
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.comment_article = article_item  # Устанавливаем связь с новостью правильно
            comment.save()
            return HttpResponseRedirect(reverse('articles:article_detail', args=[article_item.pk,]))
    return HttpResponseRedirect(reverse('articles:article_detail', args=[article_item.pk,]))


# Если не найдено, то редирект на "не найдено"
def article_not_found(request):
    return render(request, 'articles/not_found.html')
