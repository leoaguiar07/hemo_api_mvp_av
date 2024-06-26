# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuditlogLogentry(models.Model):
    object_pk = models.CharField(max_length=255)
    object_id = models.BigIntegerField(blank=True, null=True)
    object_repr = models.TextField()
    action = models.SmallIntegerField()
    changes = models.TextField()
    timestamp = models.DateTimeField()
    actor = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    remote_addr = models.GenericIPAddressField(blank=True, null=True)
    additional_data = models.JSONField(blank=True, null=True)
    serialized_data = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditlog_logentry'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ColetaColeta(models.Model):
    id = models.BigAutoField(primary_key=True)
    origem_tipo = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    hemocentro = models.IntegerField()
    quantidade = models.FloatField()
    data_hora = models.DateTimeField()
    tipo_sanguineo = models.CharField(max_length=20, blank=True, null=True)
    fator_rh = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    obs = models.TextField(blank=True, null=True)
    destino = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coleta_coleta'


class ColetasColeta(models.Model):
    id = models.BigAutoField(primary_key=True)
    origem_tipo = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    hemocentro = models.IntegerField()
    quantidade = models.FloatField()
    data_hora = models.DateTimeField()
    tipo_sanguineo = models.CharField(max_length=20, blank=True, null=True)
    fator_rh = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    obs = models.TextField(blank=True, null=True)
    destino = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coletas_coleta'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DoadoresDoador(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=300)
    cpf = models.CharField(unique=True, max_length=20)
    cep = models.IntegerField()
    logradouro = models.CharField(max_length=300)
    bairro = models.CharField(max_length=300)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=20, blank=True, null=True)
    localidade = models.CharField(max_length=300)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    nascimento = models.DateField()
    ultima_doacao = models.DateField(blank=True, null=True)
    login = models.CharField(unique=True, max_length=20)
    senha = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    fator_rh = models.CharField(max_length=1, blank=True, null=True)
    tipo_sanguineo = models.CharField(max_length=2, blank=True, null=True)
    peso_aproximado = models.IntegerField()
    genero = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doadores_doador'


class HemocentrosHemocentro(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(unique=True, max_length=300)
    cep = models.IntegerField()
    logradouro = models.CharField(max_length=300)
    bairro = models.CharField(max_length=300)
    numero = models.CharField(max_length=20, blank=True, null=True)
    localidade = models.CharField(max_length=300)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    complemento = models.CharField(max_length=20, blank=True, null=True)
    estoque_atual = models.FloatField()
    estoque_ideal = models.FloatField()
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hemocentros_hemocentro'
