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
    google_book_id = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    review = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"


# Modell för lässtatus
class ReadingStatus(models.Model):
    READING_CHOICE = [
        ("TOREAD", "Vill läsa"),
        ("READING", "Pågående"),
        ("READ", "Läst"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    google_book_id = models.CharField(max_length=200) 
    status = models.CharField(max_length=15, choices=READING_CHOICE)
    pages_read = models.IntegerField(default=0)
    started_at = models.DateField(blank=True, null=True)
    finished_at = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ("user", "book")

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.status})"
