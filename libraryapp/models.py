from django.db import models

class Kategorie(models.Model):
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
    syg_bg = models.CharField(max_length=20,null=True,blank=True)
    ozn_opdow = models.TextField(null=False)
    tytul = models.TextField(null=False)
    tom = models.TextField(null=True)
    rok = models.IntegerField(null=True)
    isbn_issn = models.CharField(max_length=100,null=True)
    typ = models.CharField(max_length=10, choices=TYP_CHOICES)
    dostepnosc = models.CharField(max_length=10, choices=DOSTEPNOSC_CHOICES)
    kategoria = models.ManyToManyField(Kategorie,blank=True)

    def __str__(self):
        return str(self.syg_ms)+" "+self.tytul

    class Meta:
        verbose_name = "Książki"
        verbose_name_plural = "Książki"