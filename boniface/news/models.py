from django.db import models


class Articles(models.Model):
    title = models.CharField('Название статьи', max_length=50)
    anons = models.CharField('Анонс', max_length=255)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.pk}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
