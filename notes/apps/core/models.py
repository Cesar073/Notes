from django.db import models


TITLES_LEVELS = [
    (1, "Level 1"),
    (2, "Level 2"),
    (3, "Level 3"),
    (4, "Level 4"),
    (5, "Level 5"),
    (6, "Level 6"),
]


# Create your models here.
class Page(models.Model):
    text = models.CharField(max_length=50)
    level = models.PositiveSmallIntegerField(choices=TITLES_LEVELS, default=1)


class Title(models.Model):
    text = models.CharField(max_length=100, null=False, blank=False)
    level = models.PositiveSmallIntegerField(choices=TITLES_LEVELS, default=1)
    pages = models.ManyToManyField(Page, related_name="pages")

class Paragraph(models.Model):
    text = models.TextField()
    titles = models.ManyToManyField(Title, related_name="titles")
