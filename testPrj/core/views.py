# from django.http import HttpResponse
# from .models import Item
# from django.shortcuts import render

# def simple_view(request):
#     return render(request, 'index.html')

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')