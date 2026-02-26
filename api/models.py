from django.db import models
from django.contrib.auth.models import User

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
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    review = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"


# Modell för lässtatus

