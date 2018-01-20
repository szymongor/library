from django.db import models

class Category(models.Model):
    category_id = models.CharField(max_length=200, unique=True,verbose_name=u'Id kategorii')
    category_name = models.TextField(verbose_name=u'Nazwa kategorii')

    def __str__(self):
        return self.category_id + " " + self.category_name

    class Meta:
        verbose_name = "Kategoria" #Dodaj książkę
        verbose_name_plural = "Kategorie"

class Book(models.Model):
    TYPE_CHOICES = (
        ('podręcznik', 'podręcznik'),
        ('inny', 'inny'),
        ('zbiór zadań', 'zbiór zadań'),
    )
    AVAILABILITY_CHOICES = (
        ('dostępna', 'dostępna'),
        ('wypożyczona','wypożyczona'),
        ('czytelnia','czytelnia'),
    )
    syg_ms = models.IntegerField(unique=True,null=False)
    syg_bg = models.CharField(max_length=20,null=True,blank=True, default="")
    ozn_opdow = models.TextField(null=False,verbose_name=u'Oznaczenie odpowiedzialności')
    title = models.TextField(null=False,verbose_name=u'Tytuł')
    volume = models.CharField(null=True,blank=True, default="",verbose_name=u'Tom',max_length=100)
    year = models.IntegerField(null=False,verbose_name=u'Rok')
    isbn_issn = models.CharField(max_length=100,null=True,blank=True, default="",verbose_name=u'ISBN ISSN')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, null=False,verbose_name=u'Typ')
    availability = models.CharField(max_length=10, choices=AVAILABILITY_CHOICES, null=False,verbose_name=u'Dostępność')
    categories = models.ManyToManyField(Category, null=False,verbose_name=u'Kategorie')

    def __str__(self):
        return str(self.syg_ms)+" "+self.title

    class Meta:
        verbose_name = "Książka" #Dodaj książkę
        verbose_name_plural = "Książki"

class CsvImport(models.Model):
    CSV_file = models.FileField(verbose_name=u'Plik CSV')

    def save(self, *args, **kwargs):
        pass

    def __str__(self):
        return 'Import : ' + self.CSV_file.name

    class Meta:
        verbose_name = "CSV"
        verbose_name_plural = "Importuj csv"