import csv

from django.db import IntegrityError

from ..models import Ksiazka, Kategorie

class CSVImporter:


    def importFromFile(self, file_object):
        return_str = ''
        first_line = file_object.readline()

        csvreader = csv.reader(file_object, delimiter=',', quotechar='"')

        import_type = self.chooseImportTypeByFirstLine(first_line)
        if import_type == 'ksiazki':
            for row in csvreader:
                return_str += self.rowToKsiazka(row)
        elif import_type == 'kategorie':
            for row in csvreader:
                return_str += self.rowToKategoria(row)
        elif import_type == 'przyppisaniekategorii':
            for row in csvreader:
                return_str += self.rowToPrzypisanieKategorii(row)


        #lines = file_object.readlines()
        #for line in lines:
        #    returnStr += self.lineToKsiazka(line)

        return return_str

    def chooseImportTypeByFirstLine(self,first_line):
        if 'SYG_MS' in first_line and 'TYTUL' in first_line:
            return 'ksiazki'
        elif 'KATEGORIA' in first_line:
            return 'kategorie'
        elif 'SYG_MS' in first_line and 'ID_KATEGORII' in first_line:
            return 'przyppisaniekategorii'


    def rowToKsiazka(self,row):
        importStatus = "|Ksiazka syg_ms: "
        try:
            SYG_MS = row[0]
            importStatus +=SYG_MS
            SYG_BG = row[1]
            OZN_OPDOW = row[2]
            TYTUL = row[3]
            TOM = row[4]
            ROK = row[5]
            ISBN_ISSN = row[6]
            TYP = row[7]
            DOSTEPNOSC = row[8]
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
                importStatus += "= SUCCESS|"
            except IntegrityError:
                importStatus += "= ALREADY EXISTS|"
                pass
        except IndexError:
            pass

        return importStatus

    def rowToKategoria(self,row):
        importStatus = "|Kategoria id: "
        try:
            ID_KATEGORII = row[0]
            KATEGORIA = row[1]
            try:
                kategoria = Kategorie.objects.create(id_kategorii=ID_KATEGORII)
                kategoria.kategoria = KATEGORIA
                kategoria.save()
                importStatus += "= SUCCESS|"
            except IntegrityError:
                importStatus += "= ALREADY EXISTS|"
                pass
        except IndexError:
            pass
        return importStatus


    def rowToPrzypisanieKategorii(self,row):
        importStatus = "|Przypisanie id: "
        try:
            SYG_MS = row[0]
            ID_KATEGORII = row[1]
            try:
                importStatus+=SYG_MS+":"+ID_KATEGORII
                ksiazka = Ksiazka.objects.get(syg_ms=SYG_MS)
                kategoria = Kategorie.objects.get(id_kategorii=ID_KATEGORII)
                ksiazka.kategoria.add(kategoria)
                importStatus += "= SUCCESS|"
            except:
                importStatus += "=ERROR|"
        except:
            pass

        return importStatus

