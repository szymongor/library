from ..models import Ksiazka, Kategorie

class KsiazkaDAO():
    #+query object

    def getKsiazka(self,query):
        filters = query['filters']
        ksiazka_set = Ksiazka.objects.filter(**filters)
        pagination = query['pagination']
        ksiazka_set = ksiazka_set[pagination['offset']:pagination['offset']+pagination['limit']]
        return ksiazka_set

    def addKsiazka(self,ksiazkaJSON):
        try:
            ksiazka = Ksiazka.objects.create(
                syg_ms=ksiazkaJSON['syg_ms'],
                ozn_opdow=ksiazkaJSON['ozn_opdow'],
                tytul=ksiazkaJSON['tytul'],
                rok=ksiazkaJSON['rok'],
                typ=ksiazkaJSON['typ'],
                dostepnosc=ksiazkaJSON['dostepnosc'],
            )
            if 'syg_bg' in ksiazkaJSON:
                ksiazka.syg_bg = ksiazkaJSON['syg_bg']
            if 'tom' in ksiazkaJSON:
                ksiazka.tom = ksiazkaJSON['tom']
            if 'isbn_issn' in ksiazkaJSON:
                ksiazka.isbn_issn = ksiazkaJSON['isbn_issn']

            for kategoriaId in ksiazkaJSON['kategorie']:
                kategoria = Kategorie.objects.get(id_kategorii=kategoriaId)
                ksiazka.kategoria.add(kategoria)

            ksiazka.save()
        except:
            pass

    def deleteKsiazka(self,ksiazkaId):
        try:
            ksiazka = Ksiazka.objects.get(syg_ms=ksiazkaId)
            ksiazka.delete()
        except:
            pass

    def updateKsiazka(self,ksiazkaJSON):
        try:
            ksiazka = Ksiazka.objects.get(syg_ms=ksiazkaJSON['syg_ms_old'])

            if 'syg_ms' in ksiazkaJSON:
                ksiazka.syg_ms = ksiazkaJSON['syg_ms']
            if 'syg_bg' in ksiazkaJSON:
                ksiazka.syg_bg = ksiazkaJSON['syg_bg']
            if 'ozn_opdow' in ksiazkaJSON:
                ksiazka.ozn_opdow = ksiazkaJSON['ozn_opdow']
            if 'tytul' in ksiazkaJSON:
                ksiazka.tytul = ksiazkaJSON['tytul']
            if 'tom' in ksiazkaJSON:
                ksiazka.tom = ksiazkaJSON['tom']
            if 'rok' in ksiazkaJSON:
                ksiazka.rok = ksiazkaJSON['rok']
            if 'isbn_issn' in ksiazkaJSON:
                ksiazka.isbn_issn = ksiazkaJSON['isbn_issn']
            if 'typ' in ksiazkaJSON:
                ksiazka.syg_ms = ksiazkaJSON['typ']
            if 'dostepnosc' in ksiazkaJSON:
                ksiazka.dostepnosc = ksiazkaJSON['dostepnosc']

            if 'kategorie_add' in ksiazkaJSON:
                for kategoriaId in ksiazkaJSON['kategorie_add']:
                    kategoria = Kategorie.objects.get(kategoria_id=kategoriaId)
                    ksiazka.kategoria.add(kategoria)

            if 'kategorie_remove' in ksiazkaJSON:
                for kategoriaId in ksiazkaJSON['kategorie_remove']:
                    kategoria = Kategorie.objects.get(kategoria_id=kategoriaId)
                    ksiazka.kategoria.remove(kategoria)

            ksiazka.save()
        except:
            pass

