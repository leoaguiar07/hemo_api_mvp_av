# Generated by Django 5.0.3 on 2024-04-05 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hemocentros', '0008_alter_hemocentro_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hemocentro',
            name='cep',
            field=models.IntegerField(),
        ),
    ]