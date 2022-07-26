from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    language = models.CharField(max_length=60)

    def __str__(self):
        return self.name
