# Generated by Django 5.0.3 on 2024-04-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coletas', '0003_alter_coleta_cpf_alter_coleta_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='coleta',
            name='obs',
            field=models.TextField(blank=True, null=True),
        ),
    ]
