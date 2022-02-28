from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User, Client, Vendor, Admin


# @admin.register(get_user_model())
# class CustomUserAdmin(UserAdmin):
#     pass


admin.site.register(User)
admin.site.register(Client)
admin.site.register(Vendor)
admin.site.register(Admin)
