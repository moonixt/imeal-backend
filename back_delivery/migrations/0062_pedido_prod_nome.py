# Generated by Django 4.2.7 on 2024-05-19 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_delivery', '0061_alter_pedido_data_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='prod_nome',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
