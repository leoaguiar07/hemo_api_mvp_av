# Generated by Django 5.0.3 on 2024-04-02 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('cpf', models.IntegerField()),
                ('cep', models.IntegerField()),
                ('logradouro', models.CharField(max_length=300)),
                ('bairro', models.CharField(max_length=300)),
                ('numero', models.CharField(max_length=20)),
                ('complemento', models.CharField(max_length=20)),
                ('localidade', models.CharField(max_length=300)),
                ('uf', models.CharField(max_length=2)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('nascimento', models.DateField()),
                ('ultima_doacao', models.DateField()),
                ('login', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
