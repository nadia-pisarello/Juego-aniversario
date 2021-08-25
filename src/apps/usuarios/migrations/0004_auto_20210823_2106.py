# Generated by Django 3.2.6 on 2021-08-24 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuario_puntos'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='es_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='ult_acceso',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]