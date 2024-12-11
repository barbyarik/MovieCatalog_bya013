from django import forms
from .models import Subtitle

class SubtitleForm(forms.ModelForm):
    class Meta:
        model = Subtitle
        fields = ['text', 'character', 'start_time', 'end_time']