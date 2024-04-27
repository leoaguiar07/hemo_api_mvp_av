# Generated by Django 5.0.3 on 2024-04-03 00:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hemocentros', '0006_remove_hemocentro_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='hemocentro',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
    ]
