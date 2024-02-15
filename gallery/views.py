from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Image, Category, Event
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Вывод всех объектов (названия с изображениями).
def gallery_list(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'gallery/gallery_list.html', context)


# Вывод всех объектов (названия с изображениями).
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    images = event.images.all()
    context = {'event': event, 'images': images}
    return render(request, 'gallery/event_detail.html', context)


# Загрузка нового изображения.
def image_create(request):
    if request.method == 'POST':
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_list')
    else:
        form = forms.ImageForm()
    return render(request, 'gallery/image_create.html', {'form': form})


# Вывод изображений по определённой категории.
def images_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    images = Image.objects.filter(category=category)
    context = {'category': category, 'images': images}
    return render(request, 'gallery/images_by_category.html', context)


# Вывод отдельного конкретного объекта изображения с комментариями.
# def gallery_detail(request, image_id):
#     image = get_object_or_404(Image, pk=image_id)
#     comments = image.comments.all()
#     context = {'image': image, 'comments': comments}
#     return render(request, 'gallery/gallery_detail.html', context)


def gallery_detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    comments = image.comments.all()
    form = forms.CommentForm()
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.author = request.user
            comment.save()
            return redirect('gallery:gallery_detail', image_id=image_id)
    context = {'image': image,
               'comments': comments,
               'form': form}
    return render(request, 'gallery/gallery_detail.html', context)


# Поиск категорий изображений
def search_category(request):
    query = request.GET.get('q')
    if query:
        categories = Category.objects.filter(Q(name__icontains=query))
        context = {'categories': categories}
        return render(request, 'gallery/search_results.html', context)
    else:
        # Если статьи не найдены, перенаправляем на страницу "not found"
        return redirect('gallery:category_not_found')


@login_required
# Оставление комментария на стр определённого изображения.
def add_comment_to_image(request, image_id):
    image = get_object_or_404(Image, image_id)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.author = request.user
            comment.save()
            return redirect('gallery:gallery_detail', image_id=image_id)
    else:
        form = forms.CommentForm()
    return render(request, 'gallery/add_comment_to_image.html', {'form': form})


#  Если объект не найден, то редирект на "не найдено"
def category_not_found(request):
    pass
