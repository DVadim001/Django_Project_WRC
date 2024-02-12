from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('partners/', views.partners, name='partners'),
    path('signup/', views.signup, name='signup'),
    path('privacy/', views.privacy_policy, name='privacy_policy'),
    path('terms/', views.terms_of_use, name='terms_of_use'),

]