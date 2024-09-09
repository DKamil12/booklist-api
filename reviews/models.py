from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        self.book.update_rating()

    def __str__(self) -> str:
        return f'{self.user} on {self.book}'