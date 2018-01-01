import csv

from django.db import IntegrityError

from ..models import Ksiazka, Kategorie
from .ImportStatus import ImportStatus, ImportStatusCollection

class CSVImporter:


    def importFromFile(self, file_object):
        import_status_collection = ImportStatusCollection()
        first_line = file_object.readline()

        csvreader = csv.reader(file_object, delimiter=',', quotechar='"')

        import_type = self.chooseImportTypeByFirstLine(first_line)
        if import_type == 'ksiazki':
            for row in csvreader:
                import_status = self.rowToKsiazka(row).getStatus()
                import_status_collection.addImportStatus(import_status)
        elif import_type == 'kategorie':
            for row in csvreader:
                import_status = self.rowToKategoria(row).getStatus()
                import_status_collection.addImportStatus(import_status)
        elif import_type == 'przyppisaniekategorii':
            for row in csvreader:
                import_status = self.rowToPrzypisanieKategorii(row).getStatus()
                import_status_collection.addImportStatus(import_status)



        #lines = file_object.readlines()
        #for line in lines:
        #    returnStr += self.lineToKsiazka(line)

        return import_status_collection

    def chooseImportTypeByFirstLine(self,first_line):
        if 'SYG_MS' in first_line and 'TYTUL' in first_line:
            return 'ksiazki'
        elif 'KATEGORIA' in first_line:
            return 'kategorie'
        elif 'SYG_MS' in first_line and 'ID_KATEGORII' in first_line:
            return 'przyppisaniekategorii'


    def rowToKsiazka(self,row):
        importStatus = ImportStatus()
        try:
            SYG_MS = row[0]
            SYG_BG = row[1]
            OZN_OPDOW = row[2]
            TYTUL = row[3]
            TOM = row[4]
            ROK = row[5]
            ISBN_ISSN = row[6]
            TYP = row[7]
            DOSTEPNOSC = row[8]
            importStatus.setAction("Ksiazka syg_ms:" + SYG_MS)
            try:
                ksiazka = Ksiazka.objects.create(
                    syg_ms=SYG_MS,
                )
                if(SYG_BG != ''):
                    ksiazka.syg_bg = SYG_BG
                ksiazka.ozn_opdow = OZN_OPDOW
                ksiazka.tytul = TYTUL
                if(TOM != ''):
                    ksiazka.tom = TOM
                if(ROK != ''):
                    ksiazka.rok = ROK
                ksiazka.isbn_issn = ISBN_ISSN
                ksiazka.typ = TYP
                ksiazka.dostepnosc = DOSTEPNOSC
                ksiazka.save()
                importStatus.setResult("Success")
            except IntegrityError:
                importStatus.setResult("Already exits")
                pass
        except IndexError:
            pass

        return importStatus

    def rowToKategoria(self,row):
        importStatus = ImportStatus()
        try:
            ID_KATEGORII = row[0]
            KATEGORIA = row[1]
            importStatus.setAction("Kategoria id:" + ID_KATEGORII)
            try:
                kategoria = Kategorie.objects.create(id_kategorii=ID_KATEGORII)
                kategoria.kategoria = KATEGORIA
                kategoria.save()
                importStatus.setResult("Success")
            except IntegrityError:
                importStatus.setResult("Already exits")
                pass
        except IndexError:
            pass
        return importStatus


    def rowToPrzypisanieKategorii(self,row):
        importStatus = ImportStatus()
        try:
            SYG_MS = row[0]
            ID_KATEGORII = row[1]
            importStatus.setAction("Przypisanie syg_ms: "+SYG_MS+" id kat:"+ID_KATEGORII)
            try:
                ksiazka = Ksiazka.objects.get(syg_ms=SYG_MS)
                kategoria = Kategorie.objects.get(id_kategorii=ID_KATEGORII)
                ksiazka.kategoria.add(kategoria)
                importStatus.setResult("Success")
            except:
                importStatus.setResult("Already exits")
        except:
            pass

        return importStatus

