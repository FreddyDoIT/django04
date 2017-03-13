from django.db import models
from django.contrib.auth.models import User
class ActivateCode(models.Model):
    owner = models.ForeignKey(User, verbose_name="用户名")
    code = models.CharField("激活码", max_length=100)
    expire_timestamp = models.DateTimeField("过期时间")