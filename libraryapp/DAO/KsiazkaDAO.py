from ..models import Ksiazka

class KsiazkaDAO():
    #+query object

    def getKsiazka(self,query):
        filters = query['filters']
        ksiazka_set = Ksiazka.objects.filter(**filters)
        pagination = query['pagination']
        ksiazka_set = ksiazka_set[pagination['offset']:pagination['offset']+pagination['limit']]
        return ksiazka_set

