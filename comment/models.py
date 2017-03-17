from django.db import models
from django.contrib.auth.models import User
from article.models import Article

class Comment(models.Model):
    owner = models.ForeignKey(User, verbose_name="评论作者")
    article = models.ForeignKey(Article, verbose_name="所评论文章")
    content = models.CharField("评论内容",max_length=10000)
    status = models.IntegerField("状态",
                                 choices=((0, "正常"), (-1, "删除")), default=0)
    create_timestamp = models.DateTimeField("评论创建时间", auto_now_add=True)
    last_update_timestamp = models.DateTimeField("评论更新时刻", auto_now=True)
    to_comment = models.ForeignKey("self", null=True, blank=True, verbose_name="回复评论的功能")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"