from django.db import models
from django.db.models.fields import CharField, DateTimeField

from cms import settings


class Admin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = CharField(max_length=255, blank=False, null=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        db_table = 'admin'

    def __str__(self):
        return self.name
