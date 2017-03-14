from django.shortcuts import render
from block.models import Block
from .models import Article
from django.shortcuts import redirect
from .forms import ArticleForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles_objs = Article.objects.filter(block=block, status=0).order_by("-id")

    ARTICLE_CNT_1PAGE = 2 #定义一页有多少条数据
    page_no = int(request.GET.get("page_no", "1")) #获取参数
    all_articles = Article.objects.filter(block=block, status=0).order_by("-id") #全量数据
    p=Paginator(all_articles, ARTICLE_CNT_1PAGE) #把全量数据和每页数据数给分页器，得到分页器实例p
    page = p.page(page_no) #把页码参数给分页器的page方法，得到页码变量page，代表分好的一页（每一个页）
    articles_objs = page.object_list #分号的每页中取出其数据——页中的文章
    page_links = [i for i in range(page_no-5, page_no+6) if i > 0 and i <= p.num_pages]

    return render(request, "article_list.html",
                  {"articles": articles_objs, "b": block,
                   "p__p": p, "p__page": page, "p__links": page_links})

@login_required
def article_create(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == "GET":
        return render(request, "article_create.html", {"b": block})
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.owner = request.user
            article.block = block
            article.status = 0
            article.save()
            return redirect("/article/list/%s" % block_id)
        else:
            return render(request, "article_create.html", {"b": block, "form": form})


def article_detail(request, a_id):
    article = Article.objects.get(id=a_id)
    return render(request, "article_detail.html", {"article_detail": article})
