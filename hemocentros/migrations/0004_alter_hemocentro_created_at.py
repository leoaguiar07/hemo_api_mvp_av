# Generated by Django 5.0.3 on 2024-04-02 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hemocentros', '0003_alter_hemocentro_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hemocentro',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
