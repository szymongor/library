from django.db import IntegrityError
from django.db.models import QuerySet

from libraryapp.CSVImporter.ResponseStatus import ResponseStatusCollection, ResponseStatus
from ..models import Book, Category

class BookDAO():

    def get_book(self, query):
        filters = query['filters']
        categories = query['categories']
        books_by_categories = Book.objects.all()
        if len(categories) != 0:
            books_by_categories = Book.objects.none()
            for category in categories:
                books_by_categories = books_by_categories | Book.objects.filter(categories__category_id=category)
        book_query_set = books_by_categories.filter(**filters)
        [upper_case_filters, lower_case_fitlers] = self.upperLowerCaseFilters(filters)
        book_query_set = book_query_set | books_by_categories.filter(**upper_case_filters)
        book_query_set = book_query_set | books_by_categories.filter(**lower_case_fitlers)

        pagination = query['pagination']
        book_query_set = book_query_set[pagination['offset']:pagination['offset']+pagination['limit']]
        return book_query_set

    # def add_book(self, book_json):
    #     response_status = ResponseStatus()
    #     response_status.setAction("Adding ksiazka: " + book_json['syg_ms'])
    #     try:
    #         ksiazka = Ksiazka.objects.create(
    #             syg_ms=book_json['syg_ms'],
    #             ozn_opdow=book_json['ozn_opdow'],
    #             tytul=book_json['tytul'],
    #             rok=book_json['rok'],
    #             typ=book_json['typ'],
    #             dostepnosc=book_json['dostepnosc'],
    #         )
    #         if 'syg_bg' in book_json:
    #             ksiazka.syg_bg = book_json['syg_bg']
    #         if 'tom' in book_json:
    #             ksiazka.tom = book_json['tom']
    #         if 'isbn_issn' in book_json:
    #             ksiazka.isbn_issn = book_json['isbn_issn']
    #
    #         for kategoriaId in book_json['kategorie']:
    #             kategoria = Kategoria.objects.get(id_kategorii=kategoriaId)
    #             ksiazka.kategoria.add(kategoria)
    #
    #         ksiazka.save()
    #         response_status.setResult("Success")
    #     except IntegrityError:
    #         response_status.setResult("Ksiazka already exists")
    #     except:
    #         response_status.setResult("Unknown error")
    #     return response_status
    #
    # def deleteKsiazka(self,ksiazkaId):
    #     try:
    #         ksiazka = Ksiazka.objects.get(syg_ms=ksiazkaId)
    #         ksiazka.delete()
    #     except:
    #         pass
    #
    # def updateKsiazka(self,ksiazkaJSON):
    #     try:
    #         ksiazka = Ksiazka.objects.get(syg_ms=ksiazkaJSON['syg_ms_old'])
    #
    #         if 'syg_ms' in ksiazkaJSON:
    #             ksiazka.syg_ms = ksiazkaJSON['syg_ms']
    #         if 'syg_bg' in ksiazkaJSON:
    #             ksiazka.syg_bg = ksiazkaJSON['syg_bg']
    #         if 'ozn_opdow' in ksiazkaJSON:
    #             ksiazka.ozn_opdow = ksiazkaJSON['ozn_opdow']
    #         if 'tytul' in ksiazkaJSON:
    #             ksiazka.tytul = ksiazkaJSON['tytul']
    #         if 'tom' in ksiazkaJSON:
    #             ksiazka.tom = ksiazkaJSON['tom']
    #         if 'rok' in ksiazkaJSON:
    #             ksiazka.rok = ksiazkaJSON['rok']
    #         if 'isbn_issn' in ksiazkaJSON:
    #             ksiazka.isbn_issn = ksiazkaJSON['isbn_issn']
    #         if 'typ' in ksiazkaJSON:
    #             ksiazka.syg_ms = ksiazkaJSON['typ']
    #         if 'dostepnosc' in ksiazkaJSON:
    #             ksiazka.dostepnosc = ksiazkaJSON['dostepnosc']
    #
    #         if 'kategorie_add' in ksiazkaJSON:
    #             for kategoriaId in ksiazkaJSON['kategorie_add']:
    #                 kategoria = Kategoria.objects.get(kategoria_id=kategoriaId)
    #                 ksiazka.kategoria.add(kategoria)
    #
    #         if 'kategorie_remove' in ksiazkaJSON:
    #             for kategoriaId in ksiazkaJSON['kategorie_remove']:
    #                 kategoria = Kategoria.objects.get(kategoria_id=kategoriaId)
    #                 ksiazka.kategoria.remove(kategoria)
    #
    #         ksiazka.save()
    #     except:
    #         pass

    def upperLowerCaseFilters(self,filters):
        new_filters_upper = {}
        new_filters_lower = {}
        for field in filters:
            new_filters_upper[field] = filters[field].upper()
            new_filters_lower[field] = filters[field].lower()
        return [new_filters_lower,new_filters_upper]
