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


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'
    KINDS = (
        (EMAIL, 'Email'),
        (PHONE, 'Telefone'),
    )
    speaker = models.ForeignKey("Speaker", on_delete=models.CASCADE, verbose_name='palestrante')
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    value = models.CharField('valor', max_length=60)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.value
