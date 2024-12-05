from django.db import models
from films.models import Film

class Subtitle(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name="Фильм")
    text = models.TextField(verbose_name="Текст")
    character = models.CharField(max_length=100, blank=True, verbose_name="Персонаж")
    start_time = models.FloatField(verbose_name="Время начала (сек.)")
    end_time = models.FloatField(verbose_name="Время окончания (сек.)")

    def cropped_text(self, text):
        return f"{text if len(text) < 51 else text[:50]+'...'}"

    def __str__(self):
        return f"Субтитр для фильма «{self.film.name}»: {self.cropped_text(self.text)}"
    
    class Meta:
        ordering = ['film', 'start_time']
        verbose_name = "Субтитр"
        verbose_name_plural = "Субтитры"