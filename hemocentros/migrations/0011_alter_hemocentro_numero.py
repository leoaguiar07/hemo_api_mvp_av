# Generated by Django 5.0.3 on 2024-04-05 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hemocentros', '0010_hemocentro_complemento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hemocentro',
            name='numero',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]