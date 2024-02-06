from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test_events(request):
    return HttpResponse('Тест events')
