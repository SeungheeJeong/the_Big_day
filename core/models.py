from django.db import models


class TimeStampedModel(models.Model):
    """Time Stamped Model"""
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:  # DB에는 저장하지 않고 사용하고 싶은 데이터를 만든다
        abstract = True
