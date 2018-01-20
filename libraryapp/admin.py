from django.contrib import admin
from .models import Book
from .models import Category
from django.utils.translation import ugettext_lazy
from django.contrib import admin
from .models import CsvImport
from django.contrib import messages
from io import TextIOWrapper
from .CSVImporter.CSVImporter import CSVImporter


class LogEntryAdmin(object):
    pass


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
            if import_status['result'] == "Sukces":
                style = messages.SUCCESS
            elif import_status['result'] == "Już istnieje":
                style = messages.WARNING
            else:
                style = messages.ERROR
            messages.add_message(request, style,
                                 "Importowanie: "+import_status['action']+". "+
                                "Status: "+import_status['result']+".")

    def has_change_permission(cls, request, obj=None):
        ''' remove add and save and add another button '''
        return False



class KsiazkaAdmin(admin.ModelAdmin):
    list_display = ('syg_ms','syg_bg','ozn_opdow', 'title',
                    'volume','year','isbn_issn','type','availability',)
    search_fields = ('syg_ms', 'title','=categories__category_id',)
    filter_horizontal = ('categories',)

class KategoriaAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_name',]
    search_fields = ('category_id',)

admin.site.register(Book, KsiazkaAdmin)
admin.site.register(CsvImport,CSVAdmin)
admin.site.register(Category, KategoriaAdmin)
admin.site.site_title = 'Administracja biblioteką'
admin.site.site_header = 'Administracja biblioteką'
admin.site.index_title = 'Administracja zasobami'
admin.site.site_url = None