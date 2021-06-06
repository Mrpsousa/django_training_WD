# Generated by Django 3.1.3 on 2021-06-06 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210604_0126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speaker',
            options={'verbose_name': 'Palestrante', 'verbose_name_plural': 'Palestrantes'},
        ),
        migrations.AlterField(
            model_name='speaker',
            name='description',
            field=models.TextField(blank=True, max_length=512, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='name',
            field=models.TextField(max_length=128, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='photo',
            field=models.URLField(verbose_name='foto'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='website',
            field=models.URLField(blank=True, verbose_name='website'),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.TextField(max_length=128, verbose_name='nome')),
                ('value', models.TextField(max_length=128, verbose_name='nome')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.speaker')),
            ],
        ),
    ]
