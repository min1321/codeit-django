# 데이터 베이스와 연동을 관리하는 파일

from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    img_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name
