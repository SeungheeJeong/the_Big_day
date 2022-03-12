from django.contrib import admin
from . import models


@admin.register(models.Recruit)
class RecruitAdmin(admin.ModelAdmin):
    pass
    # admin.site.register(Recruit)

    # Register your models here.


@admin.register(models.Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    pass
