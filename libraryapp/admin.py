from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

from .models import Book
from .models import Category
from django.contrib import admin
from .models import CsvImport
from django.contrib import messages
from io import TextIOWrapper
from .CSVImporter.CSVImporter import CSVImporter


class CSVAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        file = request.FILES['CSV_file']
        file_obj = TextIOWrapper(file, encoding=request.encoding)
        importer = CSVImporter()
        result = importer.importFromFile(file_obj)
        self.addMessage(request,result)

    def addMessage(self,request,import_result):
        imports = import_result.get_import_status()
        for import_status in imports:
            if import_status['result'] == "SUCCES":
                style = messages.SUCCESS
            elif import_status['result'] == "INFO":
                style = messages.INFO
            elif import_status['result'] == "WARNING":
                style = messages.WARNING
            else:
                style = messages.ERROR
            messages.add_message(request, style,
                                 "Importowanie: "+import_status['action']+". "+
                                "Status: "+import_status['message']+".")

    def has_change_permission(cls, request, obj=None):
        ''' remove add and save and add another button '''
        return False






class KsiazkaAdmin(admin.ModelAdmin):
    list_display = ('signature_ms','signature_bg','responsibility', 'title',
                    'volume','year','isbn_issn','type','availability',)
    search_fields = ('=signature_ms', 'title','=categories__category_id','categories__category_name')
    filter_horizontal = ('categories',)

    def save_model(self, request, obj, form, change):
        if '_pass' in request.POST:
            messages.set_level(request, messages.WARNING)
            messages.warning(request, 'Nie zapisano zmian')
            return redirect('/libraryapp/book')

        else:
            return super().save_model(request, obj, form, change)

    class Media:
        css = {
            'all': ('css/resize-widget.css',),
        }
        js = ['js/resize-widget.js','js/add-pass-button.js']

class KategoriaAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_name',]
    search_fields = ('category_id', 'category_name',)

    def save_model(self, request, obj, form, change):
        if '_pass' in request.POST:
            messages.set_level(request, messages.WARNING)
            messages.warning(request, 'Nie zapisano zmian')
            return redirect('/libraryapp/category')

        else:
            return super().save_model(request, obj, form, change)

    class Media:
        js = ['js/add-pass-button.js']

admin.site.register(Book, KsiazkaAdmin)
admin.site.register(CsvImport, CSVAdmin)
admin.site.register(Category, KategoriaAdmin)
admin.site.site_title = 'Administracja biblioteką'
admin.site.site_header = 'Administracja biblioteką'
admin.site.index_title = 'Administracja zasobami'
admin.site.site_url = None
