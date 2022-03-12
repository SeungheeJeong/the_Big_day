from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    """Custom Challenge Admin"""
    list_display = (
        "subject",
        "status",
        "host",
        "routine",
        "num_of_auth_per_day",
        "date_start",
        "date_finish",
        "created",
    )

    list_filter = (
        "status",
        "host",
        "date_start",
    )


@admin.register(models.Photo)
class Photo(admin.ModelAdmin):
    """Photo Admin Definition """
    list_display = (
        '__str__',
        'get_thumbnail',
        'created',
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}"/>')

    get_thumbnail.short_description = "Thumbnail"
