# Generated by Django 2.2.2 on 2019-07-09 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20190630_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(max_length=250, unique=True, verbose_name='Slug'),
        ),
    ]