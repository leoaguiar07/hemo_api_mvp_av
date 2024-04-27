# Generated by Django 5.0.3 on 2024-04-02 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hemocentro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300, unique=True)),
                ('cep', models.CharField(max_length=9)),
                ('logradouro', models.CharField(max_length=300)),
                ('bairro', models.CharField(max_length=300)),
                ('numero', models.CharField(max_length=20)),
                ('localidade', models.CharField(max_length=300)),
                ('uf', models.CharField(max_length=2)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]