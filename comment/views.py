from .models import Comment
from .responses import json_response
from article.models import Article

def create_comment(request):

    if not request.user.is_authenticated():#判断是否一登录；这句是若没有登录的话……
        return json_response({"status": "error",
                              "message": "您还没有登录，不能发表评论"})

    article_id = int(request.POST["article_id"])
    content = request.POST["content"].strip()

    if not content:
        return json_response({"status": "error", "message": "评论内容不能为空"})

    article = Article.objects.get(id=article_id)

    comment = Comment(article=article, owner=request.user, content=content)
    comment.save()

    return json_response({"status":"okay","message":""})


