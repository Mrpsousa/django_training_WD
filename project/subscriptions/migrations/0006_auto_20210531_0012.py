# Generated by Django 3.1.3 on 2021-05-31 00:12

from django.db import migrations, models
import project.subscriptions.validators


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0005_auto_20210524_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='cpf',
            field=models.CharField(max_length=11, validators=[project.subscriptions.validators.validate_cpf], verbose_name='cpf'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='telefone'),
        ),
    ]