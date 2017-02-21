from django.db import models

class Block(models.Model):
    name = models.CharField(u"板块名称",max_length=100)
    descp = models.CharField(u"板块描述",max_length=100)
    admin_name=models.CharField(u"板块管理员名称",max_length=100)