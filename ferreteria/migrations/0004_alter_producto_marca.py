# Generated by Django 4.2.2 on 2024-05-15 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferreteria', '0003_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.CharField(max_length=100),
        ),
    ]
