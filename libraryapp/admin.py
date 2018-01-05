from django.contrib import admin
from .models import Ksiazka
from .models import Kategorie
from django.utils.translation import ugettext_lazy


def deleteKatrgoria(self, modeladmin, request, queryset):
    pass

deleteKatrgoria.short_description = "Delete Kategoria"

class KsiazkaAdmin(admin.ModelAdmin):
    list_display = ['syg_ms', 'tytul']
    #raw_id_fields = ("kategoria",)
    filter_horizontal = ('kategoria',)
    actions=[deleteKatrgoria]

admin.site.register(Ksiazka, KsiazkaAdmin)
admin.site.register(Kategorie)
admin.site.site_title = 'Administracja biblioteką'
admin.site.site_header = 'Administracja biblioteką'
admin.site.index_title = 'Administracja stoną'