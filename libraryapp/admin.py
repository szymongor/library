from django.contrib import admin
from .models import Ksiazka
from .models import Kategoria
from django.utils.translation import ugettext_lazy
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
        imports = import_result.getImportStatus()
        for import_status in imports:
            if import_status['result'] == "Success":
                style = messages.SUCCESS
            elif import_status['result'] == "Already exits":
                style = messages.WARNING
            else:
                style = messages.ERROR
            messages.add_message(request, style,
                                 "Importing: "+import_status['action']+". "+
                                "Status: "+import_status['result']+".")


class KsiazkaAdmin(admin.ModelAdmin):
    list_display = ('syg_ms','syg_bg','ozn_opdow', 'tytul',
                    'tom','rok','isbn_issn','typ','dostepnosc',)
    search_fields = ('syg_ms', 'tytul','=kategoria__id_kategorii',)
    filter_horizontal = ('kategoria',)

class KategoriaAdmin(admin.ModelAdmin):
    list_display = ['id_kategorii', 'kategoria',]
    search_fields = ('id_kategorii',)

admin.site.register(Ksiazka, KsiazkaAdmin)
admin.site.register(CsvImport,CSVAdmin)
admin.site.register(Kategoria, KategoriaAdmin)
admin.site.site_title = 'Administracja biblioteką'
admin.site.site_header = 'Administracja biblioteką'
admin.site.index_title = 'Administracja stoną'