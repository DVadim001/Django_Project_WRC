from django.shortcuts import render, redirect
# from . import forms
from .models import Event, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View

from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from django.http import HttpResponse

from django.shortcuts import get_object_or_404


# # Вывод всех событий

# Вывод события по определённой категории
def events_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    events = category.category_event.all()
    context = {'category': category, 'events': events}
    return render(request, 'event_by_category.html', context)


# Вывод отдельной конкретной новости
def event(request, pk):
    try:
        event = Event.objects.get(id=pk)
    except Event.DoesNotExist:
        raise Http404('К сожалению, Событие не найдена')
    comments = event.comments_event.order_by('-id')
    context = {'event': event, 'comments': comments}
    return render(request, 'events/event.html', context)


# Поиск новостей по фильтру
def search_event(request):
    if request.method == 'POST':
        get_event = request.POST.get('search_event')
        event = Event.objects.filter(event_title__icontains=get_event)
        if event: # Проверяет, содержит ли запрос объекты
            # Если статьи найдены, рендер страницы с результатами поиска
            context = {'event': event}
            return render(request, 'search_result.html', context)
        else:
            # Если статьи не найдены, перенаправляем на страницу "not found"
            return redirect('/not_found')


# Оставление комментария на стр определённого события
def comment(request, pk):
    try:
        comm_e = Event.objects.get(id=pk)
    except:
        raise Http404('Новость не найдена.')
    comm_e.comments_event.create(comment_author_event=request.POST['name'], comment_text_event=request.POST['text'])
    return HttpResponseRedirect(reverse('event:event_detail', args=(comm_e.id,)))


# Если не найдено, то редирект на "не найдено"
def event_not_found(request):
    return render(request, 'not_found.html')

