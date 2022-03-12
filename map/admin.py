from django.contrib import admin
from . import models


@admin.register(models.Maps)
class MapAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "name",
        "kakaourl",
        "pageurl",
    )
