from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Tenisky(models.Model):
    nazev = models.CharField(max_length=100, verbose_name="Název tenisek", help_text='Zadejte text o maximální délce 100 znaků')
    popis = models.TextField(blank=True, null=True, verbose_name="Popis")
    cena = models.FloatField(validators=[MinValueValidator(0.0)], null=True, help_text="Zadejte nezáporné desetinné číslo", verbose_name="Nákupní cena")
    cena1 = models.FloatField(validators=[MinValueValidator(0.0)], null=True, help_text="Zadejte nezáporné desetinné číslo", verbose_name="Přeprodejní cena")
    VELIKOST = (
        (40, 'EU 40, US 7'),
        (41, 'EU 41, US 8'),
        (42, 'EU 42, US 8.5'),
        (43, 'EU 43, US 9.5'),
        (44, 'EU 44, US 10'),
        (45, 'EU 45 , US 11'),
        (46, 'EU 46, US 12'),
        (47, 'EU 47, US 13'),
    )
    velikost = models.IntegerField(max_length=1, choices=VELIKOST, blank=True, default=3, verbose_name="Velikost tenisek", help_text='Vyberte velikost')
    foto = models.ImageField(upload_to='tenisky/%Y/%m/%d/', blank=True, null=True, verbose_name="Fotka")

    class Meta:
        ordering = ["nazev"]
        verbose_name = 'Zboží'
        verbose_name_plural = 'Zboží'

    def __str__(self):
        return f"{self.nazev}, {self.cena}"

    def get_absolute_url(self):
        """Metoda vrací URL stránky, na které se vypisují podrobné informace o zboží"""
        return reverse('detail', args=[str(self.id)])
