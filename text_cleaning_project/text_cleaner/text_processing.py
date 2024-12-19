import requests
from difflib import SequenceMatcher

def is_similar(word1, word2, threshold=0.8):
    """
    Проверяет схожесть двух слов по коэффициенту сходства.
    :param word1: Первое слово.
    :param word2: Второе слово.
    :param threshold: Пороговое значение (0-1).
    :return: True, если слова схожи, иначе False.
    """
    return SequenceMatcher(None, word1.lower(), word2.lower()).ratio() >= threshold

def correct_spelling_yandex(text, lang="en"):
    """
    Исправляет текст с помощью Яндекс.Спеллера.
    :param text: Текст для проверки.
    :param lang: Язык текста ("ru", "en", "uk").
    :return: Исправленный текст.
    """
    url = "https://speller.yandex.net/services/spellservice.json/checkText"
    params = {"text": text, "lang": lang}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        corrections = response.json()
        
        if not corrections:
            return text
        
        for correction in corrections:
            word = correction["word"]
            suggestions = correction["s"]
            
            # Пропускаем исправления, если они не похожи на исходное слово
            if suggestions and is_similar(word, suggestions[0]):
                text = text.replace(word, suggestions[0])
        
        return text
    except requests.RequestException as e:
        print(f"Error: {e}")
        return text