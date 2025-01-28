# from django.http import HttpResponse
# from .models import Item
# from django.shortcuts import render

# def simple_view(request):
#     return render(request, 'index.html')

from django.shortcuts import render



def language_selection(request):
    return render(request, 'lang.html')

def russian_page(request):
    return render(request, 'index_ru.html')

def english_page(request):
    return render(request, 'index_en.html')