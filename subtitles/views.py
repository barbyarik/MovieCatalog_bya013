from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .forms import SubtitleForm
from .models import Subtitle
from .models import Subtitle
from films.models import Film
import json

@staff_member_required
def create_subtitle(request):
    if request.method == 'POST':
        form = SubtitleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_subtitle_success')
    else:
        form = SubtitleForm()
    return render(request, 'subtitles/create_subtitle.html', {'form': form})


def create_subtitle_success(request):
    return render(request, 'subtitles/create_subtitle_success.html')


@staff_member_required
def edit_subtitle(request, subtitle_id):
    subtitle = get_object_or_404(Subtitle, pk=subtitle_id)
    if request.method == 'POST':
        form = SubtitleForm(request.POST, instance=subtitle)
        if form.is_valid():
            form.save()
            return redirect('create_subtitle_success')
    else:
        form = SubtitleForm(instance=subtitle)
    return render(request, 'subtitles/edit_subtitle.html', {'form': form})


@staff_member_required
def delete_subtitle(request, subtitle_id):
    subtitle = get_object_or_404(Subtitle, pk=subtitle_id)
    if request.method == 'POST':
        subtitle.delete()
        return redirect('delete_subtitle_success')
    return render(request, 'subtitles/delete_subtitle.html', {'subtitle': subtitle})


def delete_subtitle_success(request):
    return render(request, 'subtitles/delete_subtitle_success.html')