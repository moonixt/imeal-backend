# Generated by Django 4.2.7 on 2024-05-19 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_delivery', '0065_alter_pedido_prod_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='prod_nome',
            field=models.CharField(max_length=50),
        ),
    ]
