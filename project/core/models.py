from django.db import models
from django.shortcuts import resolve_url as r


class Speaker(models.Model):
    name = models.TextField('nome', max_length=128)
    slug = models.SlugField('slug')
    website = models.URLField('website', blank=True)
    photo = models.URLField('foto')
    description = models.TextField('descrição', max_length=512, blank=True)

    class Meta:
        verbose_name = 'Palestrante'
        verbose_name_plural = "Palestrantes"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)

# Create your models here.
