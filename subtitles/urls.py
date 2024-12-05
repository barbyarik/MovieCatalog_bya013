from django.urls import path
from . import views

urlpatterns = [
    path('create_subtitle/', views.create_subtitle, name='create_subtitle'),
    path('create_subtitle/success/', views.create_subtitle_success, name='create_subtitle_success'),
    path('edit_subtitle/<int:subtitle_id>/', views.edit_subtitle, name='edit_subtitle'),
    path('delete_subtitle/<int:subtitle_id>/', views.delete_subtitle, name='delete_subtitle'),
    path('delete_subtitle/success/', views.delete_subtitle_success, name='delete_subtitle_success'),
]