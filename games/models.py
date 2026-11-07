from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    release_date = models.DateField()
    developer = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    genres = models.ManyToManyField('Genre', blank=True)
    platforms = models.ManyToManyField('platforms.Platform', blank=True)

    class Meta:
        ordering = ['title']

    image = models.ImageField(
        upload_to='games/',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
