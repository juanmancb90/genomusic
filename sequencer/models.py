from django.db import models


class Sequence(models.Model):
    """ Sequence Model
    """
    DB_CHOICES = (
        ('protein', 'protein'),
        ('nucleotide', 'nucleotide'),
    )
    name = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )
    db = models.CharField(
        max_length=500,
        choices=DB_CHOICES,
        null=True,
        blank=True
    )
    query_key = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )
    web_env = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )
    header = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )
    raw = models.TextField()
    active = models.BooleanField(default=True)
