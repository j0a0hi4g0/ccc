# Generated by Django 4.1.7 on 2023-04-13 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0003_delete_listacompras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aplicacao',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
