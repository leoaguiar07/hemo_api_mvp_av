# Generated by Django 5.0.3 on 2024-04-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coletas', '0005_coleta_destino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coleta',
            name='destino',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
    ]
