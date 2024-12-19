from django.contrib import admin
from .models import TextData

@admin.register(TextData)
class TextDataAdmin(admin.ModelAdmin):
    list_display = ('original_text', 'language', 'created_at')  # Отображаемые поля в админке
    search_fields = ('original_text',)  # Возможность поиска по исходному тексту ))