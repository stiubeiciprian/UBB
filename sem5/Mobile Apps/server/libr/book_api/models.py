from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    number_of_pages = models.PositiveIntegerField()
    current_page = models.PositiveIntegerField()
    genres = models.CharField(max_length=255)

    def __str__(self):
        return self.title
