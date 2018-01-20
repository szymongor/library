from rest_framework import serializers

from libraryapp.DAO.CategoriesTree import CategoriesTree
from .models import Book, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        #fields = '__all__'
        fields= ('category_id', 'category_name')

class BookSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Book
        #fields='__all__'
        fields=('syg_ms','syg_bg','ozn_opdow','title',
                'volume','year','isbn_issn','type','availability',
                'categories',)

class CategoryTreeSerializer(serializers.Serializer):
    category = CategorySerializer(many=False, read_only=True)
    subcategories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = CategoriesTree
        fields = '__all__'