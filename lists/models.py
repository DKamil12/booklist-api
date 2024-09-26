from typing import Any, Iterable
from django.db import models
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.
class List(models.Model):
    user = models.ForeignKey(User, related_name='lists', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    followers_count = models.PositiveIntegerField(default=0)
    # books = models.ManyToManyField(Book)

    def subscribe(self):
        self.followers_count += 1
        self.save()

    def unsubscribe(self):
        self.followers_count -= 1
        self.save()

    def __str__(self) -> str:
        return f'{self.name} by {self.user}'


class ListItem(models.Model):
    list = models.ForeignKey(List, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='list_items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.book.title} in {self.list}'


class ListFollower(models.Model):
    user = models.ForeignKey(User, related_name='followed_lists', on_delete=models.CASCADE)
    list = models.ForeignKey(List, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'list'], name='unique_user_list_follow')
        ]

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        self.list.subscribe()
        
    def delete(self, *args, **kwargs) -> None:
        super().delete(*args, **kwargs)
        self.list.unsubscribe()

    def __str__(self) -> str:
        return f'{self.user} follows {self.list}'
