from django.db import models


class Author(models.Model):
    fullname = models.CharField(blank=False, unique=True)
    born_date = models.CharField(blank=True)
    born_location = models.CharField(blank=True)
    description = models.CharField(blank=True)


class Quote(models.Model):
    tags = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote = models.CharField(blank=False)
