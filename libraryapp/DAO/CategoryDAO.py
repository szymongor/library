from libraryapp.DAO.CategoriesTree import CategoriesTree
from ..models import Book, Category

class CategoryDAO:

    def get_category(self):
        main_categories = self.get_main_categories()
        categories = []
        for main_category in main_categories:
            subcategories = self.get_subcategories(main_category)
            category_tree = CategoriesTree(main_category, subcategories)
            categories.append(category_tree)
        return categories

    def get_main_categories(self):
        main_categories = Category.objects.exclude(category_id__contains="-").extra(\
    select={'lower_name':'lower(category_name)'}).order_by('lower_name')
        return main_categories

    def get_subcategories(self, main_category):
        subcategory_id=main_category.category_id + "-"
        subcategories = Category.objects.filter(category_id__contains=subcategory_id).extra( \
            select={'lower_name': 'lower(category_name)'}).order_by('lower_name')
        return subcategories