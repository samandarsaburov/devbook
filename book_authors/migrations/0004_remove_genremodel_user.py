# Generated by Django 4.2.5 on 2023-09-08 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0003_alter_authermodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genremodel',
            name='user',
        ),
    ]
