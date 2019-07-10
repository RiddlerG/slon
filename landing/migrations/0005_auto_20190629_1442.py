# Generated by Django 2.2.2 on 2019-06-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20190629_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailfromstring',
            name='host',
            field=models.CharField(max_length=250, verbose_name='EMAIL_HOST'),
        ),
        migrations.AlterField(
            model_name='mailfromstring',
            name='host_password',
            field=models.CharField(max_length=250, verbose_name='EMAIL_HOST_PASSWORD'),
        ),
        migrations.AlterField(
            model_name='mailfromstring',
            name='host_user',
            field=models.EmailField(max_length=250, verbose_name='EMAIL_HOST_USER'),
        ),
        migrations.AlterField(
            model_name='mailfromstring',
            name='port',
            field=models.PositiveIntegerField(verbose_name='EMAIL_PORT'),
        ),
        migrations.AlterField(
            model_name='mailfromstring',
            name='use_ssl',
            field=models.BooleanField(verbose_name='EMAIL_USE_SSL(yandex.ru)'),
        ),
        migrations.AlterField(
            model_name='mailfromstring',
            name='use_tls',
            field=models.BooleanField(verbose_name='EMAIL_USE_TLS(gmail.com, mail.ru)'),
        ),
    ]