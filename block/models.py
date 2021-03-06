from django.db import models


class Block(models.Model):
    name = models.CharField("版块名称",max_length=100)
    descp = models.CharField("版块描述",max_length=100)
    admin = models.CharField("版块管理员名称",max_length=100)
    status = models.IntegerField("状态",choices=((0,"正常"),(-1,"删除")))



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "版块"
        verbose_name_plural = "版块（列表）"