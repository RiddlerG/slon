from django.db import models


class CallBack(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Время заяки')

    class Meta:
        verbose_name = 'Звонок'
        verbose_name_plural = 'Звонки'

    def __str__(self):
        return '%s' % self.phone