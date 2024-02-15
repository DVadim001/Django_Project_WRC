from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
    path('', views.gallery_list, name='gallery_list'),
    path('<int:image_id>/', views.gallery_detail, name='gallery_detail'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('category/<int:category_id>/', views.images_by_category, name='images_by_category'),
    path('search/', views.search_category, name='search_category'),
    path('image/create/', views.image_create, name='image_create'),
    path('image/<int:pk>/comment/', views.add_comment_to_image, name='add_comment_to_image'),

]
