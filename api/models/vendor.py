from django.db import models
from django.db.models.fields import CharField, DateTimeField

from cms import settings


class Vendor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = CharField(max_length=255, blank=False, null=False)
    address = CharField(max_length=200, default='')
    phone = CharField(max_length=20, default='')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        db_table = 'vendors'

    def __str__(self):
        return self.name
