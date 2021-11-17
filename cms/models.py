from django.db import models
from django.contrib.auth.models import User,Group
from django.utils import timezone


# Create your models here.
class UserHealth(models.Model):
    """ユーザーのBMI"""
    #name=models.CharField("名前",max_length=64)
    name = models.ForeignKey(User,verbose_name='名前', on_delete=models.CASCADE)
    Height = models.DecimalField("身長", max_digits=4, decimal_places=1)
    Weight = models.DecimalField("体重", max_digits=4, decimal_places=1)
    date = models.DateField(verbose_name='実施日', default=timezone.localtime, blank=True, null=True, )
    BMI = models.DecimalField("BMI", max_digits=4, decimal_places=2)
    condition = models.CharField("状態", max_length=256)

    def __str__(self):
        return self.name