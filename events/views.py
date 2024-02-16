from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Event, Category
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .handlers import bot
from django.contrib.auth.models import User


# Вывод всех событий на основной странице по событиям
def main_event(request):
    search = forms.SearchForm()
    events = Event.objects.order_by('-event_date')
    context = {'search': search, 'events': events}
    return render(request, 'events/event_list.html', context)


# Вывод события по определённой категории
def events_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    events = category.category_event.all()
    context = {'category': category, 'events': events}
    return render(request, 'events/event_by_category.html', context)


# Вывод отдельной конкретной новости
def event(request, pk):
    event_item = get_object_or_404(Event, pk=pk)
    comments = event_item.comments_event.order_by('-id')
    if request.method == 'POST':
        # Создаём экземпляр формы и заполняем его данными из запроса:
        comment_form = forms.CommentForm(request.POST)
        # Проверяем валидность формы:
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # Сразу в БД не сохраняем
            comment.event = event_item # Привязываем комментарий к конкретной новости
            comment.save() # Теперь сохраняем
            return redirect('events:event_detail', pk=event_item.pk) # Перенаправляем обратно к новости
    else:
        comment_form = forms.CommentForm() # Создаём пустой экземпляр формы для GET-запроса

    # Добавляем форму комментария в текст
    context = {'event': event_item,
               'comments': comments,
               'comment_form': comment_form}
    return render(request, 'events/event.html', context)


# Поиск новостей по фильтру
def search_event(request):
    if 'search_query' in request.GET:
        get_event = request.GET.get('search_query')
        events = Event.objects.filter(event_title__icontains=get_event)
        if event: # Проверяет, содержит ли запрос объекты
            # Если статьи найдены, рендер страницы с результатами поиска
            context = {'events': events}
            return render(request, 'events/search_result.html', context)
        else:
            # Если статьи не найдены, перенаправляем на страницу "not found"
            return redirect('events:event_not_found')


# Оставление комментария на стр определённого события зарегистрированным пользователем
@login_required
def comment(request, pk):
    event_item = Event.objects.filter(pk=pk).first()
    if not event_item:
        raise Http404('Событие не найдено.')
    if request.method == "POST":
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.comment_event = event_item  # Устанавливаем связь с новостью правильно
            comment.save()
            return HttpResponseRedirect(reverse('events:event_detail', args=[event_item.pk,]))
    return HttpResponseRedirect(reverse('events:event_detail', args=[event_item.pk,]))


# Если не найдено, то редирект на "не найдено"
def event_not_found(request):
    return render(request, 'events/not_found.html')


# Отправка заявки в тг
def send_telegram_message(user_id, event_id):
    # Получаем объекты по ID
    user = User.objects.get(pk=user_id)
    event = Event.objects.get(pk=event_id)
    # Формируем текстсообщения
    text = f"Пользователь {user.username} ({user.first_name} {user.last_name}) хочет принять участие в событии '{event.title}'."
    user_id = 82836904
    bot.send_message(user_id=user_id, text=text)


# Обработка функции подачи заявки на событие
@login_required
def event_participate(request, event_id):
    if request.method == 'POST':
        user_id = request.user.id
        send_telegram_message(user_id, event_id)
        return redirect('events:event_detail', pk=event_id)
