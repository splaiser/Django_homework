from django.db import models

from django.db.models import ManyToManyField


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")


class Scope(models.Model):
    tag = ManyToManyField(Tag, related_name="scopes")
    is_main = models.BooleanField(verbose_name='Основной раздел')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    scopes = ManyToManyField(Scope, related_name='articles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title
