from django import forms
from .models import TextData

class TextDataForm(forms.ModelForm):
    class Meta:
        model = TextData  # Связываем форму с моделью TextData
        fields = ['original_text', 'language']  # Поля, которые будут отображаться в форме
        widgets = {
            'original_text': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Введите текст для обработки...'}),
            'language': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'original_text': 'Исходный текст',
            'language': 'Язык текста',
        }



# TextDataForm — это форма, связанная с моделью TextData.
# Поля:
# original_text: Поле для ввода исходного текста.
# language: Выпадающий список для выбора языка.
# Виджеты (widgets) позволяют настроить внешний вид полей формы (например, добавить атрибуты HTML).
# Метки (labels) задают пользовательские названия для полей формы.