# Generated by Django 5.0.3 on 2024-04-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doadores', '0013_alter_doador_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='doador',
            name='latitude',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='doador',
            name='longitude',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
