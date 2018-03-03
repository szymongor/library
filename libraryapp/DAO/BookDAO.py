from django.db import IntegrityError
from django.db.models import QuerySet

from libraryapp.CSVImporter.ResponseStatus import ResponseStatusCollection, ResponseStatus
from ..models import Book, Category

class BookDAO():

    def get_book(self, query):
        filters = query['filters']
        self.process_filters(filters)
        categories = query['categories']
        books_by_categories = Book.objects.all()#.order_by('title', 'year')
        if len(categories) != 0:
            books_by_categories = Book.objects.none()
            for category in categories:
                books_by_categories = books_by_categories | Book.objects.filter(categories__category_id=category)
        book_query_set = books_by_categories.filter(**filters).order_by('title', 'year')
        [upper_case_filters, lower_case_fitlers] = self.upperLowerCaseFilters(filters)
        book_query_set = book_query_set | books_by_categories.filter(**upper_case_filters)
        book_query_set = book_query_set | books_by_categories.filter(**lower_case_fitlers)
        pagination = query['pagination']
        book_query_set = book_query_set[pagination['offset']:pagination['offset']+pagination['limit']]
        return book_query_set

    def process_filters(self, filters):
        self.delete_blank_filters(filters)
        self.case_insensitive_filter(filters)

    def delete_blank_filters(self, filters):
        remove = [key for key in filters if filters[key] == ""]
        for key in remove: del filters[key]

    def case_insensitive_filter(self,filters):
        for field in filters:
            if '__' not in field:
                filters[field+'__iexact'] = filters.pop(field)
                continue

    def upperLowerCaseFilters(self,filters):
        new_filters_upper = {}
        new_filters_lower = {}
        for field in filters:
            new_filters_upper[field] = filters[field].upper()
            new_filters_lower[field] = filters[field].lower()
        return [new_filters_lower,new_filters_upper]

