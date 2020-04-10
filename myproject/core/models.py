from django.db import models


class Language(models.Model):
    'id',
    'name',
    'creator',
    'year',
    'typed',

    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100, null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    typed = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'linguagem'
        verbose_name_plural = 'linguagens'

    def __str__(self):
        return self.name
