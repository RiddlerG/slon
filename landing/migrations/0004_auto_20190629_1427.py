# Generated by Django 2.2.2 on 2019-06-29 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_mailfromstring_mailtostring'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailfromstring',
            old_name='email_host',
            new_name='host',
        ),
        migrations.RenameField(
            model_name='mailfromstring',
            old_name='email_host_password',
            new_name='host_password',
        ),
        migrations.RenameField(
            model_name='mailfromstring',
            old_name='email_host_user',
            new_name='host_user',
        ),
        migrations.RenameField(
            model_name='mailfromstring',
            old_name='email_port',
            new_name='port',
        ),
        migrations.RenameField(
            model_name='mailfromstring',
            old_name='email_use_ssl',
            new_name='use_ssl',
        ),
        migrations.RenameField(
            model_name='mailfromstring',
            old_name='email_use_tls',
            new_name='use_tls',
        ),
    ]