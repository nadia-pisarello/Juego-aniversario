# Generated by Django 3.2.6 on 2021-08-26 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_alter_usuario_is_valid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='is_valid',
        ),
    ]