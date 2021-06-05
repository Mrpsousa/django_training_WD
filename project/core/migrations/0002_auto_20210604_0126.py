# Generated by Django 3.1.3 on 2021-06-04 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='photo',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='website',
            field=models.URLField(),
        ),
    ]