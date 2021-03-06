# Generated by Django 2.2.2 on 2019-06-30 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
        ('landing', '0007_aboutus_ourpros'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedFlatPage',
            fields=[
                ('flatpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='flatpages.FlatPage')),
                ('my_order', models.PositiveIntegerField(default=0, verbose_name='Сортировка')),
                ('seo_title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Title')),
                ('desc', models.CharField(blank=True, max_length=250, null=True, verbose_name='Description')),
                ('keywords', models.CharField(blank=True, max_length=250, null=True, verbose_name='Keywords')),
            ],
            options={
                'verbose_name': 'Простая страница',
                'verbose_name_plural': 'Простые страницы',
                'ordering': ['my_order'],
            },
            bases=('flatpages.flatpage',),
        ),
    ]
