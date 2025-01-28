"""
URL configuration for testPrj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import language_selection, russian_page, english_page 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', language_selection, name='language_selection'),  # Стартовая страница
    path('ru/', russian_page, name='russian_page'),  # Русская версия
    path('en/', english_page, name='english_page'),  # Английская версия
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
