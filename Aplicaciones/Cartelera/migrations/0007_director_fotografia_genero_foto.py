# Generated by Django 4.0.6 on 2024-06-26 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0006_alter_pelicula_duracion'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='fotografia',
            field=models.FileField(blank=True, null=True, upload_to='director'),
        ),
        migrations.AddField(
            model_name='genero',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='generos'),
        ),
    ]
