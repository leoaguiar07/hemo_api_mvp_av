# Generated by Django 5.0.3 on 2024-04-03 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hemocentros', '0007_hemocentro_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hemocentro',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
