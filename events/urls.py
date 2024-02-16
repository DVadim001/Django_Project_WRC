from django.urls import path
from . import views

app_name = 'events'
urlpatterns = [
    path('', views.main_event, name='event_list'),
    path('<int:pk>/', views.event, name='event_detail'),
    path('search/', views.search_event, name='search_events'),
    path('not_found/', views.event_not_found, name='event_not_found'),
    path('event/<int:pk>/comment/', views.comment, name='event_comment'),
    path('category/<int:category_id>/', views.events_by_category, name='events_by_category'),
    path('event/<int:event_id>/participate/', views.event_participate, name='event_participate'),
]
