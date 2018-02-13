from django.db import models

class Category(models.Model):
    category_id = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Id kategorii'
    )
    category_name = models.TextField(
        verbose_name='Nazwa kategorii'
    )

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
    signature_ms = models.IntegerField(
        unique=True,
        null=False,
        verbose_name='Sygnatura ms'
    )
    signature_bg = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        default="",
        verbose_name='Sygnatura bg'
    )
    responsibility = models.TextField(
        null=False,
        verbose_name='Oznaczenie odpowiedzialności'
    )
    title = models.TextField(
        null=False,
        verbose_name='Tytuł'
    )
    volume = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        default="",
        verbose_name='Tom'
    )
    year = models.IntegerField(
        null=False,
        verbose_name='Rok'
    )
    isbn_issn = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        default="",
        verbose_name='ISBN ISSN'
    )
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        null=False,
        verbose_name='Typ'
    )
    availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        null=False,
        verbose_name='Dostępność'
    )
    categories = models.ManyToManyField(
        Category,
        null=False,
        verbose_name='Kategorie'
    )

    def __str__(self):
        return str(self.signature_ms) + " " + self.title

    class Meta:
        verbose_name = "Książka"
        verbose_name_plural = "Książki"

class CsvImport(models.Model):
    CSV_file = models.FileField(verbose_name='Plik CSV')

    def save(self, *args, **kwargs):
        pass

    def __str__(self):
        return self.CSV_file.name

    class Meta:
        verbose_name = "CSV"
        verbose_name_plural = "Importuj csv"