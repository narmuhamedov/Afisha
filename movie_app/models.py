from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Director(models.Model):
    name = models.CharField(max_length=50)

    @property
    def count_movies(self):
        return self.movies.all().count()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE,
                                 related_name='movies')
    def __str__(self):
        return self.title

    @property
    def count_reviews(self):
        return self.reviews.all().count()


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])


    def __str__(self):
        return self.text

    # @property
    # def average_reviews(self):
    #     return sum((self.stars.all())) / (self.stars.all().count())