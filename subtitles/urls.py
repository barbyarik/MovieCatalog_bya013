from django.urls import path
from .views import SubtitleListView, SubtitleCreateView,\
SubtitleUpdateView, SubtitleDeleteView

app_name = 'subtitles'
urlpatterns = [
    path('<int:film_id>/list/', SubtitleListView.as_view(), name='subtitle_list'),
    path('<int:film_id>/add/', SubtitleCreateView.as_view(), name='subtitle_add'),
    path('<int:film_id>/<int:pk>/edit/', SubtitleUpdateView.as_view(), name='subtitle_edit'),
    path('<int:film_id>/<int:pk>/delete/', SubtitleDeleteView.as_view(), name='subtitle_delete'),
]