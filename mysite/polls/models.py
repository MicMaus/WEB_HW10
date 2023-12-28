from django.db import models


class Author(models.Model):
    fullname = models.CharField(blank=False, unique=True)
    born_date = models.CharField()
    born_location = models.CharField()
    description = models.CharField()


class Quote(models.Model):
    tags = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote = models.CharField(blank=False)
