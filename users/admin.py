from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile",
            {"fields":
                ("birthdate",
                 "avatar",
                 "takencourse",
                 "hp")}),
    )
