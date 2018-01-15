from rest_framework import serializers

from libraryapp.DAO.KategoriaTree import KategoriaTree
from .models import Ksiazka, Kategoria


class KategorieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kategoria
        #fields = '__all__'
        fields= ('id_kategorii', 'kategoria')

class KsiazkaSerializer(serializers.ModelSerializer):
    #kategoria = serializers.StringRelatedField(many=True)
    kategoria = KategorieSerializer(many=True, read_only=True)

    class Meta:
        model = Ksiazka
        #fields='__all__'
        fields=('syg_ms','syg_bg','ozn_opdow','tytul',
                'tom','rok','isbn_issn','typ','dostepnosc',
                'kategoria',)

class KategoriaTreeSerializer(serializers.Serializer    ):
    kategoria = KategorieSerializer(many=False, read_only=True)
    podkategorie = KategorieSerializer(many=True, read_only=True)

    class Meta:
        model = KategoriaTree
        fields = '__all__'