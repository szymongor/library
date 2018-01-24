import csv

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db import IntegrityError

from ..models import Book, Category
from .ResponseStatus import ResponseStatus, ResponseStatusCollection

BOOKS = 'BOOKS'
CATEGORIES = 'CATEGORIES'
CATEGORIES_ASSIGNMENT = 'CATEGORIES_ASSIGNMENT'

class CSVImporter:


    def importFromFile(self, file_object):
        import_status_collection = ResponseStatusCollection()
        first_line = file_object.readline()

        csv_reader = csv.reader(file_object, delimiter=',', quotechar='"')

        import_type = self.choose_import_type_by_first_line(first_line)
        if import_type == BOOKS:
            for row in csv_reader:
                import_status = self.row_to_book(row).get_status()
                import_status_collection.add_import_status(import_status)
        elif import_type == CATEGORIES:
            for row in csv_reader:
                import_status = self.row_to_category(row).get_status()
                import_status_collection.add_import_status(import_status)
        elif import_type == CATEGORIES_ASSIGNMENT:
            for row in csv_reader:
                import_status = self.row_to_category_assignment(row).get_status()
                import_status_collection.add_import_status(import_status)

        file_object.close()
        return import_status_collection

    def choose_import_type_by_first_line(self, first_line):
        if 'SYG_MS' in first_line and 'TYTUL' in first_line:
            return BOOKS
        elif 'KATEGORIA' in first_line:
            return CATEGORIES
        elif 'SYG_MS' in first_line and 'ID_KATEGORII' in first_line:
            return CATEGORIES_ASSIGNMENT


    def row_to_book(self, row):
        import_status = ResponseStatus()
        try:
            SYG_MS = row[0]
            SYG_BG = row[1]
            RESPONSIBILITY = row[2]
            TITLE = row[3]
            VOLUME = row[4]
            YEAR = row[5]
            ISBN_ISSN = row[6]
            TYPE = row[7]
            AVAILABILITY = row[8]
            import_status.set_action("Książka syg_ms:" + SYG_MS)
            try:
                with transaction.atomic():
                    book = Book.objects.create(
                        signature_ms=SYG_MS,
                        responsibility=RESPONSIBILITY,
                        title=TITLE,
                        year=YEAR,
                        type=TYPE,
                        availability=AVAILABILITY,
                    )
                    if(SYG_BG != ''):
                        book.signature_bg = SYG_BG
                    if(VOLUME != ''):
                        book.volume = VOLUME
                    if (ISBN_ISSN != ''):
                        book.isbn_issn = ISBN_ISSN

                    book.save()
                    import_status.set_result("SUCCES")
                    import_status.set_message("Sukces")
            except IntegrityError:
                import_status.set_result("WARNING")
                import_status.set_message("Już istnieje")
            except Exception as e:
                import_status.set_result("ERROR")
                import_status.set_message("Nieznany błąd: " + str(e))
        except IndexError:
            pass

        return import_status

    def row_to_category(self, row):
        import_status = ResponseStatus()
        try:
            CATEGORY_ID = row[0]
            CATEGORY_NAME = row[1]
            import_status.set_action("Kategoria id: " + CATEGORY_ID)
            try:
                with transaction.atomic():
                    category = Category.objects.create(category_id=CATEGORY_ID)
                    category.category_name = CATEGORY_NAME
                    category.save()
                    import_status.set_result("SUCCES")
                    import_status.set_message("Sukces")
            except IntegrityError:
                category = Category.objects.get(category_id=CATEGORY_ID)
                if category.category_name == CATEGORY_NAME:
                    import_status.set_result("WARNING")
                    import_status.set_message("Już istnieje")
                else:
                    category.category_name = CATEGORY_NAME
                    category.save()
                    import_status.set_result("INFO")
                    import_status.set_message("Zmieniono nazwę kategorii")

            except Exception as e:
                import_status.set_result("ERROR")
                import_status.set_message("Nieznany błąd: "+ str(e))

        except IndexError:
            pass
        return import_status


    def row_to_category_assignment(self, row):
        import_status = ResponseStatus()
        try:
            SYG_MS = row[0]
            CATEGORY_ID = row[1]
            import_status.set_action("Przypisanie syg_ms: " + SYG_MS + "+ id kat: " + CATEGORY_ID)
            try:
                with transaction.atomic():
                    book = Book.objects.get(signature_ms=SYG_MS)
                    category = Category.objects.get(category_id=CATEGORY_ID)
                    book.categories.add(category)
                    import_status.set_result("SUCCES")
                    import_status.set_message("Sukces")
            except ObjectDoesNotExist:
                import_status.set_result("ERROR")
                import_status.set_message("Nie ma takiej książki lub kategorii")
            except IntegrityError:
                import_status.set_result("WARNING")
                import_status.set_message("Już istnieje to przypisanie")
            except Exception as e:
                import_status.set_result("ERROR")
                import_status.set_message("Nieznany błąd: "+ str(e))
        except:
            pass

        return import_status

