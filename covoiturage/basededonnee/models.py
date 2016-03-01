from django.db import models
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Parent(models.Model):
    Nom = models.CharField(max_length=30)
    Prenom = models.CharField(max_length=30)
    Adresse = models.CharField(max_length=100)
    Nom_de_compte = models.CharField(max_length=30)
    mot_de_passe = models.CharField(max_length=42)
   # photo = models.ImageField(upload_to="photos/", default=os.path.join(BASE_DIR,'media/default'))
    def __str__(self):
        return self.Nom


class Enfant(models.Model):
    Nom = models.CharField(max_length=30)
    Prenom = models.CharField(max_length=30)
    Nom_de_compte = models.CharField(max_length=30)
    mot_de_passe = models.CharField(max_length=42)
    parent = models.ForeignKey(Parent)
    def __str__(self):
        return self.Nom
