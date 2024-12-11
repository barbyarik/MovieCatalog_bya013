from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .forms import SubtitleForm
from .models import Subtitle
from .models import Subtitle
from films.models import Film
import json

from django.shortcuts import get_object_or_404, redirect, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Subtitle
from films.models import Film
from .forms import SubtitleForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class SubtitleListView(LoginRequiredMixin, ListView):
    model = Subtitle
    template_name = 'subtitles/subtitle_list.html'
    context_object_name = 'subtitles'

    def get_queryset(self):
        self.film = get_object_or_404(Film, pk=self.kwargs['film_id'])
        return Subtitle.objects.filter(film=self.film)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['film'] = self.film
        return context

class SubtitleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView, ListView):
    model = Subtitle
    form_class = SubtitleForm
    template_name = 'subtitles/subtitle_form.html'

    def get_queryset(self):
        self.film = get_object_or_404(Film, pk=self.kwargs['film_id'])
        return Subtitle.objects.filter(film=self.film)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['film'] = self.film
        return context

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        form.instance.film = get_object_or_404(Film, pk=self.kwargs['film_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('films:subtitles:subtitle_list', kwargs={'film_id': self.kwargs['film_id']})

class SubtitleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Subtitle
    form_class = SubtitleForm
    template_name = 'subtitles/subtitle_update.html'

    def get_queryset(self):
        self.film = get_object_or_404(Film, pk=self.kwargs['film_id'])
        return Subtitle.objects.filter(film=self.film)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['film'] = self.film
        return context

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        return reverse('films:subtitles:subtitle_list', kwargs={'film_id': self.kwargs['film_id']})

class SubtitleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Subtitle
    template_name = 'subtitles/subtitle_delete.html'

    def get_queryset(self):
        self.film = get_object_or_404(Film, pk=self.kwargs['film_id'])
        return Subtitle.objects.filter(film=self.film)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['film'] = self.film
        return context

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        film_id = self.object.film.id
        return reverse('films:subtitles:subtitle_list', kwargs={'film_id': film_id})