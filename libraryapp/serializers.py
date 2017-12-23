from rest_framework import serializers
from .models import Ksiazka, Kategorie

class KsiazkaSerializer(serializers.ModelSerializer):
    kategoria = serializers.StringRelatedField(many=True)

    class Meta:
        model = Ksiazka
        #fields=('syg_ms','tytul')
        fields='__all__'

class KategorieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kategorie
        fields = '__all__'