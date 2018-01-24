from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from libraryapp import views

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('books', views.KsiazkaList.as_view()),
    path('categories', views.KategoriaList.as_view()),
    path('dictionary', views.DictionaryView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
