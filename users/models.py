from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


class User(AbstractUser):
    COURSE_BIGDATA = "bigdata"
    COURSE_AI = "ai"
    COURSE_CLOUD = "cloud"
    COURSE_IOT = "iot"
    COURSE_CHOICES = (
        (COURSE_BIGDATA, "빅데이터 프로젝트과정"),
        (COURSE_AI, "AI 프로젝트과정"),
        (COURSE_CLOUD, "클라우드 프로젝트과정"),
        (COURSE_IOT, "IOT 프로젝트과정")
    )
    birthdate = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    takencourse = models.CharField(
        choices=COURSE_CHOICES, max_length=20, null=True, blank=True)
    hp = models.CharField(max_length=11, null=True, blank=True)
    score = models.IntegerField(default=0)
