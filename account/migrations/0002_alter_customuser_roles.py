# Generated by Django 4.2.5 on 2023-09-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='roles',
            field=models.PositiveSmallIntegerField(choices=[(3, 'admin'), (2, 'writer'), (1, 'reader')], default=1),
        ),
    ]