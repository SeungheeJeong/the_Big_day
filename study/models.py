from django.db import models


class Algorithm(models.Model):
    subject = models.CharField(max_length=200)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.subject
