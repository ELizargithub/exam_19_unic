from django.urls import path
from . import views

urlpatterns = [
    path('', views.process_text, name='process_text'),  # Главная страница обработки текста
    path('result/<int:pk>/', views.result, name='result'),  # Страница результата обработки текста
]