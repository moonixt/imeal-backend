# Generated by Django 4.2.7 on 2024-05-19 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back_delivery', '0067_remove_pedido_prod_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='restaurante',
        ),
        migrations.AddField(
            model_name='pedido',
            name='restaurante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='back_delivery.restaurante'),
            preserve_default=False,
        ),
    ]
