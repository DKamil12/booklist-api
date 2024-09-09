from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    # generate bio

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    poster = models.ImageField(
        upload_to='images',
        blank=True,
        null=True
    )
    avg_rating = models.FloatField(default=0)
    # min-max validator
    created_at = models.DateTimeField(auto_now_add=True)

    def update_rating(self):
        reviews = self.reviews.all()
        total_rating = sum(review.rating for review in reviews)
        rating_count = reviews.count()
        self.avg_rating = total_rating / rating_count
        self.save()

    def __str__(self) -> str:
        return f'{self.title} by {self.author}'

        