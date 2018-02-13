from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    category_id = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Id kategorii',
        help_text="Aby dodać podkategorię,"
                  +" należy wpisać id kategorii głównej i po myślniku id podkategorii,"
                  +" np 'G_00-S_00'"
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
        validators=[MinValueValidator(1000)],
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
        default=TYPE_CHOICES[1][0],
        null=False,
        verbose_name='Typ'
    )
    availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        default=AVAILABILITY_CHOICES[0][0],
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

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.xml']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Plik powinien mieć rozszerzenie .CSV')

class CsvImport(models.Model):
    CSV_file = models.FileField(verbose_name='Plik CSV',validators=[validate_file_extension])

    def save(self, *args, **kwargs):
        pass

    def __str__(self):
        return self.CSV_file.name



    class Meta:
        verbose_name = "CSV"
        verbose_name_plural = "Importuj csv"