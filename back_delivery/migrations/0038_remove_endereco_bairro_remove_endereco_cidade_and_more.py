# Generated by Django 4.2.7 on 2024-04-16 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back_delivery', '0037_restaurante_cep_restaurante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='bairro',
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='endereco_usuario',
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='uf',
        ),
    ]
