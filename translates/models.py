from django.db import models


class Label(models.Model):
    """Portal labels."""
    text = models.TextField(unique=True)

    class Meta:
        ordering = ['text']

    def __str__(self):
        return self.text


class Translation(models.Model):
    """Translated labels."""
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    english = models.TextField('English')
    spanish = models.TextField('Spanish')

    class Meta:
        ordering = ['label__text']

    def __str__(self):
        return f'en: {self.english}'
