from django.db import models

# Modell för bok 
class Book(models.Model):
    google_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(blank=True, null=True)
    pages= models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

# Modell för recension


# Modell för lässtatus

