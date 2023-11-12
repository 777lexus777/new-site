from django.shortcuts import render


def index(request):   # Главная страница
    return render(request, 'main/index.html')


def abaut(request):    # О нас
    return render(request, 'main/abaut.html')


