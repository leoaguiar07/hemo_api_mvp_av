from django.db import models

class AuditLogLogentry(models.Model):
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


    def __str__(self):
        return self.object_id


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


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)
