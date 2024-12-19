from django.db import models

class TextData(models.Model):
    original_text = models.TextField()
    cleaned_text = models.TextField(blank=True, null=True)
    LANGUAGE_CHOICES = [
        ('ru', 'Русский'),
        ('en', 'Английский'),
    ]
    language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES, default='auto')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_text[:50]
