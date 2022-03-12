from django.contrib import admin
from . import models


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
