# Generated by Django 4.1.1 on 2022-09-22 21:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='cellphone',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Número Celular'),
        ),
        migrations.AddField(
            model_name='user',
            name='identificacion',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True, verbose_name='Cédula o Ruc'),
        ),
        migrations.AddField(
            model_name='user',
            name='razon_social',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre o Razon Social'),
        ),
        migrations.AddField(
            model_name='user',
            name='reference',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Referencia'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
