from django.db import models
from datetime import date
from django.urls import reverse
from tinymce.models import HTMLField
from landing.models import SEOOptimizable


class News(SEOOptimizable):
    title = models.CharField(max_length=250, unique=True, verbose_name='Название')
    short_desc = models.CharField(max_length=250, verbose_name='Краткое описание')
    text = HTMLField(verbose_name='Текст')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    date = models.DateField(default=date.today, verbose_name='Дата создания')
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (slugify(self.title), ext)
        return 'images/news/%s' % filename

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')

    def get_absolute_url(self):
        return reverse('news_detail', args=[self.slug])

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('date',)

    def __str__(self):
        return '%s' % self.title