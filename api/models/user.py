from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField, EmailField

from api.manager import UserManager

USER_TYPE = (
    ('admin', 'Admin'),
    ('client', 'Client'),
    ('vendor', 'Vendor'),
)


class User(AbstractUser):
    username = CharField(max_length=255, unique=True, blank=False, null=False)
    email = EmailField(unique=True, blank=False, null=False)
    user_type = CharField(max_length=20, choices=USER_TYPE)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'auth_user'

