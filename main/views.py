from django.shortcuts import render


# Отображение главной страницы
def index(request):
    return render(request, 'main/index.html')


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