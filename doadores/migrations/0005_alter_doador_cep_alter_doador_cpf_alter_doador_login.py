# Generated by Django 5.0.3 on 2024-04-03 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doadores', '0004_alter_doador_cep_alter_doador_complemento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doador',
            name='cep',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='doador',
            name='cpf',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='doador',
            name='login',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]