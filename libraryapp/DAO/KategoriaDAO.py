from libraryapp.DAO.KategoriaTree import KategoriaTree
from ..models import Ksiazka, Kategoria

class KategoriaDAO:

    def getKategoria(self):
        kategorie_glowne = self.getKategoriaGlowna()
        kategorie = []
        for kategoria_glowna in kategorie_glowne:
            podkategorie = self.getPodkategorie(kategoria_glowna)
            kategoriaTree = KategoriaTree(kategoria_glowna,podkategorie)
            kategorie.append(kategoriaTree)
        return kategorie

    def getKategoriaGlowna(self):
        kategorie_glowne = Kategoria.objects.exclude(id_kategorii__contains="-")
        return kategorie_glowne

    def getPodkategorie(self,kategoria):
        kategoria_sub_id=kategoria.id_kategorii + "-"
        podkategorie = Kategoria.objects.filter(id_kategorii__contains=kategoria_sub_id)
        return podkategorie