# Generated by Django 3.2.6 on 2021-08-26 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0005_auto_20210825_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='id_partida',
        ),
    ]
