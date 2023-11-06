from django.db import models
from django.utils import timezone

class Voetbalspeler(models.Model):
    naam_voetballer = models.CharField(max_length=100)
    actuele_voetbalclub = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    datum_invoer = models.DateTimeField(default=timezone.now)
    datum_laatste_aanpassing = models.DateTimeField(default=timezone.now)

    def opslaan_en_publiceren(self):
        self.datum_laatste_aanpassing = timezone.now()
        self.save()

    def __str__(self):
        return self.naam_voetballer
