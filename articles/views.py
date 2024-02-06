from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test_article(request):
    return HttpResponse('Тест articles')
