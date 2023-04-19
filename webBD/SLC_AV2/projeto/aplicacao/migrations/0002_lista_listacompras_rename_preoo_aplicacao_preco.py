# Generated by Django 4.1.7 on 2023-04-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ListaCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.RenameField(
            model_name='aplicacao',
            old_name='preoo',
            new_name='preco',
        ),
    ]