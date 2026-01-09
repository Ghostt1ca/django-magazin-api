from django.db import models

# Create your models here.

class Categorie(models.Model):
    nume = models.CharField(max_length=100)

    def __str__(self):
        return self.nume

class Produs(models.Model):
    nume = models.CharField(max_length=100)
    pret = models.DecimalField(max_digits=10, decimal_places=2)
    cantitate = models.IntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        print(self.cantitate)
        return self.nume
    
