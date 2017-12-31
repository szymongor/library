from rest_framework import serializers
from .models import Ksiazka, Kategorie


class KategorieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kategorie
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
