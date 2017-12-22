from rest_framework import serializers
from .models import Ksiazka

class KsiazkaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ksiazka
        #fields=('syg_ms','tytul')
        fields='__all__'
