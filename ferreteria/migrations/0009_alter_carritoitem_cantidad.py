# Generated by Django 4.2.2 on 2024-06-04 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferreteria', '0008_carrito_carritoitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carritoitem',
            name='cantidad',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
