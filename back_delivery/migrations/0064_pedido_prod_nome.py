# Generated by Django 4.2.7 on 2024-05-19 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_delivery', '0063_remove_pedido_prod_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='prod_nome',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
