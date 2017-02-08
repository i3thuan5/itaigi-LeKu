from django.db import models


class 例句表(models.Model):
    漢字 = models.CharField(max_length=255)
    臺羅 = models.CharField(max_length=255)
    華語 = models.CharField(max_length=255)
    分詞 = models.CharField(max_length=1000)
