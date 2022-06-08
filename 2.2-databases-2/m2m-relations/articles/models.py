from django.db import models

from django.db.models import ManyToManyField


class Scope(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    scopes = models.ManyToManyField(Scope, related_name='scopes', through='Topic')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Topic(models.Model):
    tag = models.ForeignKey(Scope, related_name='tag', verbose_name="Название", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name='article', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной раздел')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
