# Generated by Django 4.2.7 on 2024-05-18 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back_delivery', '0041_alter_produto_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='num_nota_fiscal',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='pedido_usuario',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='serie_nota_fiscal',
        ),
    ]
