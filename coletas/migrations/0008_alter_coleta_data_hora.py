# Generated by Django 5.0.3 on 2024-04-14 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coletas', '0007_coleta_unidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coleta',
            name='data_hora',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
