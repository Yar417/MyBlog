from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, default='Статья')
    text = models.TextField('Текст статьи')
    date = models.DateTimeField('Дата создания', default=timezone.now)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Новость #{self.id}: {self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Contact(models.Model):
    theme = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField(max_length=3000)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.date.strftime("%d-%m-%Y ")} : {self.email}'
