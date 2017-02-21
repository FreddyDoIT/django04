from django.shortcuts import render
from block.models import Block

def index(request):
    block_info=Block.objects.all().order_by("-id")
    return render(request,"index.html",{"blocks":block_info})

