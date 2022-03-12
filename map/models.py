from secrets import choice
from unicodedata import category
from django.db import models

# 이름 url 시간 홈페이지 url


class Maps(models.Model):

    """ Map Model Definition """
    MAP_CAFE = "Cafe"
    MAP_FOOD = "FOOD"
    MAP_NOTEBOOK = "NOTEBOOK"
    MAP_CHOICE = (
        (MAP_CAFE, "Cafe"),
        (MAP_FOOD, "Food"),
        (MAP_NOTEBOOK, "Notebook")
    )
    category = models.CharField(choices=MAP_CHOICE, max_length=20)
    name = models.CharField(max_length=200)
    kakaourl = models.URLField(max_length=200)
    pageurl = models.URLField(max_length=200)


# class Cafe(models.Model):
#     name = models.CharField(max_length=200)
#     kakaourl = models.URLField(max_length=200)
#     pageurl = models.URLField(max_length=200)

#     def __str__(self):
#         return self.name


# class Food(models.Model):
#     name = models.CharField(max_length=200)
#     kakaourl = models.URLField(max_length=200)
#     pageurl = models.URLField(max_length=200)

#     def __str__(self):
#         return self.name


# class Notebook(models.Model):
#     name = models.CharField(max_length=200)
#     kakaourl = models.URLField(max_length=200)
#     pageurl = models.URLField(max_length=200)

#     def __str__(self):
#         return self.name
