from django.db import models
from block.models import Block

class Article(models.Model):
    block = models.ForeignKey(Block,verbose_name="文章ID")
    title = models.CharField("文章名称", max_length=100)
    content = models.CharField("文章内容", max_length=10000)
    status = models.IntegerField("状态",
                                 choices=((0,"正常"),(-1,"删除"))
                                 )
    author = models.CharField("Sevens", max_length=100)
    create_timestamp = models.DateField("文章创建时间", auto_now_add=True)
    last_update_timestamp = models.DateTimeField("文章更新时刻", auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章（列表）"
