# Generated by Django 4.2.7 on 2024-05-19 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back_delivery', '0062_pedido_prod_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='prod_nome',
        ),
    ]
