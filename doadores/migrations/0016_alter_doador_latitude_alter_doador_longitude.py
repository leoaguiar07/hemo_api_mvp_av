# Generated by Django 5.0.3 on 2024-04-08 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doadores', '0015_alter_doador_latitude_alter_doador_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doador',
            name='latitude',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doador',
            name='longitude',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
