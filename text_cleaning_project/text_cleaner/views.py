from django.shortcuts import render, get_object_or_404, redirect
from .models import TextData
from .text_processing import correct_spelling_yandex

def process_text(request):
    if request.method == "POST":
        original_text = request.POST.get("original_text")
        selected_language = request.POST.get("language", "ru")
        
        # Обработка текста с помощью Яндекс.Спеллера
        cleaned_text = correct_spelling_yandex(original_text, lang=selected_language)
        
        # Сохраняем данные в базу
        text_data = TextData.objects.create(
            original_text=original_text,
            cleaned_text=cleaned_text,
            language=selected_language
        )
        
        return redirect('result', pk=text_data.pk)
    
    return render(request, "process_text.html")

def result(request, pk):
    # Получаем объект TextData по его ID
    text_data = get_object_or_404(TextData, pk=pk)
    
    # Передаём объект в шаблон
    return render(request, "result.html", {"text_data": text_data})