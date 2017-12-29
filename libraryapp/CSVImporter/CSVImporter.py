import csv

from django.db import IntegrityError

from ..models import Ksiazka

class CSVImporter:

    def importFromFile(self, file_object):
        returnStr = ''
        firstLine = file_object.readline()
        csvreader = csv.reader(file_object, delimiter=',', quotechar='"')
        for row in csvreader:
            returnStr += self.rowToKsiazka(row)


        #lines = file_object.readlines()
        #for line in lines:
        #    returnStr += self.lineToKsiazka(line)

        return returnStr

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
