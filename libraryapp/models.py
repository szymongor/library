from django.db import models

class Kategoria(models.Model):
    id_kategorii = models.CharField(max_length=200, unique=True)
    kategoria = models.TextField()

    def __str__(self):
        return self.id_kategorii+" "+self.kategoria

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

class Ksiazka(models.Model):
    TYP_CHOICES = (
        ('podręcznik', 'podręcznik'),
        ('inny', 'inny'),
        ('zbiór zadań', 'zbiór zadań'),
    )
    DOSTEPNOSC_CHOICES = (
        ('dostępna', 'dostępna'),
        ('wypożyczona','wypożyczona'),
        ('czytelnia','czytelnia'),
    )
    syg_ms = models.IntegerField(unique=True,null=False)
    syg_bg = models.CharField(max_length=20,null=True,blank=True, default="")
    ozn_opdow = models.TextField(null=False)
    tytul = models.TextField(null=False)
    tom = models.TextField(null=True,blank=True, default="")
    rok = models.IntegerField(null=False)
    isbn_issn = models.CharField(max_length=100,null=True,blank=True, default="")
    typ = models.CharField(max_length=10, choices=TYP_CHOICES, null=False)
    dostepnosc = models.CharField(max_length=10, choices=DOSTEPNOSC_CHOICES, null=False)
    kategoria = models.ManyToManyField(Kategoria, null=False)

    def __str__(self):
        return str(self.syg_ms)+" "+self.tytul

    class Meta:
        verbose_name = "Książka"
        verbose_name_plural = "Książki"

class CsvImport(models.Model):
    CSV_file = models.FileField()

    def save(self, *args, **kwargs):
        pass
        ##super(DataFile, self).save(*args, **kwargs)
        ##filename = self.data.url

    class Meta:
        verbose_name = "CSV"
        verbose_name_plural = "Importuj csv"