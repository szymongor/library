from django.db import models

class Kategorie(models.Model):
    id_kategorii = models.CharField(max_length=200, unique=True)
    kategoria = models.TextField()

    def __str__(self):
        return self.id_kategorii+" "+self.kategoria

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
    tom = models.IntegerField(null=True)
    rok = models.IntegerField()
    isbn_issn = models.CharField(max_length=100,null=True)
    typ = models.CharField(max_length=10, choices=TYP_CHOICES)
    dostepnosc = models.CharField(max_length=10, choices=DOSTEPNOSC_CHOICES)

    def __str__(self):
        return str(self.syg_ms)+" "+self.tytul

class PrzypisanieKategorii(models.Model):
    syg_ms = models.ForeignKey(Ksiazka, db_column="syg_ms", to_field='syg_ms',related_name='kategorie', on_delete=models.CASCADE)
    id_kategorii = models.ForeignKey(Kategorie, db_column="id_kategorii", to_field='id_kategorii',on_delete=models.CASCADE)

    def __str__(self):
        return '%d: %s' % (self.syg_ms.syg_ms, self.id_kategorii)

    class Meta:
        unique_together = ('syg_ms', 'id_kategorii')