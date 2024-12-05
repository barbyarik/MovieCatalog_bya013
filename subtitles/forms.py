from django import forms
from .models import Subtitle

class SubtitleForm(forms.ModelForm):
    class Meta:
        model = Subtitle
        fields = ['film', 'text', 'character', 'start_time', 'end_time']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Содержание субтитра'}),
            'character': forms.TextInput(attrs={'placeholder': 'Имя персонажа, если фразу говорит один из героев'}),
            'start_time': forms.NumberInput(attrs={'step': 'any', 'placeholder': 'Время начала проигрывания субтитра в секундах'}),
            'end_time': forms.NumberInput(attrs={'step': 'any', 'placeholder': 'Время окончания проигрывания субтитра в секундах'}),
        }